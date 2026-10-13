"""
SupplyWise MVP pipeline: procurement-document RAG + supplier risk prediction.

Reuses Nexora's existing embedding model and Ollama wiring, but keeps its own
FAISS index and a plain sklearn risk model so it never touches the aerospace
pipeline or its Neo4j-backed knowledge graph.
"""
import os
import glob
import logging

import numpy as np
import pandas as pd
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from backend.vector_store import get_embeddings

logger = logging.getLogger(__name__)

DATA_DIR = "data/supplywise"
DOCS_DIR = os.path.join(DATA_DIR, "docs")
SUPPLIERS_CSV = os.path.join(DATA_DIR, "suppliers.csv")
ORDERS_CSV = os.path.join(DATA_DIR, "orders.csv")
VECTOR_STORE_PATH = os.path.join(DATA_DIR, "vector_store")

_CACHED_VECTOR_STORE = None
_CACHED_RISK_MODEL = None
_CACHED_SUPPLIER_TABLE = None


# ---------------------------------------------------------------------------
# Document RAG
# ---------------------------------------------------------------------------

def _load_docs():
    docs = []
    for path in glob.glob(os.path.join(DOCS_DIR, "*.md")) + glob.glob(os.path.join(DOCS_DIR, "*.txt")):
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        docs.append(Document(page_content=text, metadata={"source": os.path.basename(path)}))
    return docs


def build_vector_store():
    docs = _load_docs()
    splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=80)
    chunks = splitter.split_documents(docs)
    embeddings = get_embeddings()
    store = FAISS.from_documents(chunks, embeddings)
    store.save_local(VECTOR_STORE_PATH)
    return store


def get_vector_store():
    global _CACHED_VECTOR_STORE
    if _CACHED_VECTOR_STORE is not None:
        return _CACHED_VECTOR_STORE
    if os.path.exists(VECTOR_STORE_PATH):
        embeddings = get_embeddings()
        _CACHED_VECTOR_STORE = FAISS.load_local(
            VECTOR_STORE_PATH, embeddings, allow_dangerous_deserialization=True
        )
    else:
        _CACHED_VECTOR_STORE = build_vector_store()
    return _CACHED_VECTOR_STORE


def retrieve(query: str, k: int = 4):
    store = get_vector_store()
    return store.similarity_search(query, k=k)


# ---------------------------------------------------------------------------
# Supplier data + risk model
# ---------------------------------------------------------------------------

def _label_risk(row) -> str:
    """Ground-truth labeling heuristic, mirrors data/supplywise/docs/procurement_policy.md."""
    if row["on_time_delivery_rate"] < 0.75 or row["defect_rate"] > 0.06:
        return "High"
    if row["on_time_delivery_rate"] < 0.90 or row["defect_rate"] > 0.02:
        return "Medium"
    return "Low"


def load_supplier_table() -> pd.DataFrame:
    global _CACHED_SUPPLIER_TABLE
    if _CACHED_SUPPLIER_TABLE is not None:
        return _CACHED_SUPPLIER_TABLE

    suppliers = pd.read_csv(SUPPLIERS_CSV)
    orders = pd.read_csv(ORDERS_CSV)

    order_stats = orders.groupby("supplier_id").agg(
        total_orders=("order_id", "count"),
        avg_delay_days=("delivery_delay_days", "mean"),
        total_order_value=("unit_price_inr", "sum"),
    ).reset_index()

    table = suppliers.merge(order_stats, on="supplier_id", how="left").fillna(0)
    table["risk_level"] = table.apply(_label_risk, axis=1)
    _CACHED_SUPPLIER_TABLE = table
    return table


FEATURES = ["avg_lead_time_days", "defect_rate", "on_time_delivery_rate", "avg_delay_days"]


def train_risk_model():
    """Trains a small RandomForest on the labeling heuristic so predictions
    generalize to new suppliers instead of just replaying the label rule."""
    global _CACHED_RISK_MODEL
    from sklearn.ensemble import RandomForestClassifier

    table = load_supplier_table()
    X = table[FEATURES]
    y = table["risk_level"]

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    _CACHED_RISK_MODEL = model
    return model


def get_risk_model():
    global _CACHED_RISK_MODEL
    if _CACHED_RISK_MODEL is None:
        _CACHED_RISK_MODEL = train_risk_model()
    return _CACHED_RISK_MODEL


def predict_risk(supplier_row: dict) -> str:
    model = get_risk_model()
    X = pd.DataFrame([{f: supplier_row.get(f, 0) for f in FEATURES}])
    return model.predict(X)[0]


def get_feature_importance() -> dict:
    model = get_risk_model()
    return {f: round(float(v), 3) for f, v in zip(FEATURES, model.feature_importances_)}


def explain_risk(row: dict) -> list:
    """Human-readable reasons behind a risk level, grounded in the same
    thresholds published in data/supplywise/docs/procurement_policy.md -
    this is what makes the risk score auditable instead of a black box."""
    reasons = []
    otr = row.get("on_time_delivery_rate", 1.0)
    defect = row.get("defect_rate", 0.0)
    delay = row.get("avg_delay_days", 0.0)

    if otr < 0.75:
        reasons.append(f"On-time delivery rate ({otr*100:.0f}%) is below the 75% High-Risk threshold")
    elif otr < 0.90:
        reasons.append(f"On-time delivery rate ({otr*100:.0f}%) is below the 90% Low-Risk threshold")

    if defect > 0.06:
        reasons.append(f"Defect rate ({defect*100:.1f}%) exceeds the 6% High-Risk threshold")
    elif defect > 0.02:
        reasons.append(f"Defect rate ({defect*100:.1f}%) exceeds the 2% Low-Risk threshold")

    if delay > 5:
        reasons.append(f"Average delivery delay of {delay:.1f} days adds schedule risk")

    if row.get("category") in ("Metal Fabrication", "Chemicals"):
        reasons.append(f"{row['category']} suppliers are flagged for closer monitoring in company risk notes")

    if not reasons:
        reasons.append("Meets all Low Risk thresholds: strong on-time delivery and low defect rate")

    return reasons


# ---------------------------------------------------------------------------
# Semantic supplier / product matching (RAG over structured supplier data)
# ---------------------------------------------------------------------------

_CACHED_SUPPLIER_EMBEDDINGS = None
_CACHED_SUPPLIER_PROFILES = None


def _build_supplier_profiles():
    table = load_supplier_table()
    orders = pd.read_csv(ORDERS_CSV)
    profiles = []
    for _, row in table.iterrows():
        products = orders.loc[orders["supplier_id"] == row["supplier_id"], "product"].unique()
        product_str = ", ".join(products) if len(products) else "general procurement"
        text = (
            f"{row['name']} is a {row['category']} supplier based in {row['location']}. "
            f"Supplies: {product_str}. On-time delivery rate {row['on_time_delivery_rate']*100:.0f}%, "
            f"defect rate {row['defect_rate']*100:.1f}%, average lead time {row['avg_lead_time_days']} days, "
            f"risk level {row['risk_level']}."
        )
        profiles.append({"supplier_id": row["supplier_id"], "text": text})
    return profiles


def _get_supplier_embeddings():
    global _CACHED_SUPPLIER_EMBEDDINGS, _CACHED_SUPPLIER_PROFILES
    if _CACHED_SUPPLIER_EMBEDDINGS is None:
        _CACHED_SUPPLIER_PROFILES = _build_supplier_profiles()
        embeddings = get_embeddings()
        vecs = embeddings.embed_documents([p["text"] for p in _CACHED_SUPPLIER_PROFILES])
        _CACHED_SUPPLIER_EMBEDDINGS = np.array(vecs)
    return _CACHED_SUPPLIER_EMBEDDINGS, _CACHED_SUPPLIER_PROFILES


def semantic_supplier_search(query: str, k: int = 5) -> list:
    """Finds suppliers matching a natural-language requirement even when the
    exact product/category keywords differ - PRD 7.3 (semantic product/supplier
    matching), the feature that makes this more than a lookup table."""
    embeddings = get_embeddings()
    query_vec = np.array(embeddings.embed_query(query))
    matrix, profiles = _get_supplier_embeddings()

    norms = np.linalg.norm(matrix, axis=1) * (np.linalg.norm(query_vec) or 1)
    sims = matrix.dot(query_vec) / np.where(norms == 0, 1, norms)
    order = np.argsort(-sims)[:k]

    table = load_supplier_table().set_index("supplier_id")
    results = []
    for idx in order:
        supplier_id = profiles[idx]["supplier_id"]
        row = table.loc[supplier_id]
        results.append({
            "supplier_id": str(supplier_id),
            "name": str(row["name"]),
            "category": str(row["category"]),
            "location": str(row["location"]),
            "phone": str(row["phone"]),
            "website": str(row.get("website") or ""),
            "risk_level": str(row["risk_level"]),
            "on_time_delivery_rate": float(row["on_time_delivery_rate"]),
            "defect_rate": float(row["defect_rate"]),
            "avg_lead_time_days": int(row["avg_lead_time_days"]),
            "match_score": round(float(sims[idx]) * 100, 1),
        })
    return results


def compare_suppliers(name_a: str, name_b: str) -> dict:
    table = load_supplier_table()

    def find(name):
        exact = table[table["name"].str.lower() == name.lower()]
        if not exact.empty:
            return exact.iloc[0].to_dict()
        contains = table[table["name"].str.lower().str.contains(name.lower())]
        return contains.iloc[0].to_dict() if not contains.empty else None

    a, b = find(name_a), find(name_b)
    for s in (a, b):
        if s:
            s["risk_reasons"] = explain_risk(s)
    return {"a": a, "b": b}


# ---------------------------------------------------------------------------
# Dashboard aggregates
# ---------------------------------------------------------------------------

def get_dashboard_data() -> dict:
    table = load_supplier_table()
    orders = pd.read_csv(ORDERS_CSV)

    risk_counts = table["risk_level"].value_counts().to_dict()
    for lvl in ("Low", "Medium", "High"):
        risk_counts.setdefault(lvl, 0)

    category_breakdown = table.groupby("category").agg(
        supplier_count=("supplier_id", "count"),
        avg_defect_rate=("defect_rate", "mean"),
        avg_on_time_rate=("on_time_delivery_rate", "mean"),
        avg_lead_time_days=("avg_lead_time_days", "mean"),
        high_risk_count=("risk_level", lambda s: int((s == "High").sum())),
    ).reset_index().round(3).to_dict(orient="records")

    suppliers = table.to_dict(orient="records")
    for s in suppliers:
        s["risk_reasons"] = explain_risk(s)

    return {
        "total_suppliers": int(len(table)),
        "total_orders": int(len(orders)),
        "avg_lead_time_days": round(float(table["avg_lead_time_days"].mean()), 1),
        "avg_on_time_rate": round(float(table["on_time_delivery_rate"].mean()) * 100, 1),
        "risk_distribution": risk_counts,
        "category_breakdown": category_breakdown,
        "feature_importance": get_feature_importance(),
        "suppliers": sorted(
            [{k: v for k, v in s.items() if k in (
                "supplier_id", "name", "category", "location", "address", "phone", "website",
                "data_source", "avg_lead_time_days", "defect_rate", "on_time_delivery_rate",
                "total_orders", "avg_delay_days", "risk_level", "risk_reasons",
            )} for s in suppliers],
            key=lambda s: {"High": 0, "Medium": 1, "Low": 2}[s["risk_level"]],
        ),
    }


# ---------------------------------------------------------------------------
# Query answering (RAG + LLM, mirrors backend/llm_engine.py's Ollama wiring)
# ---------------------------------------------------------------------------

def answer_query(query: str) -> dict:
    chunks = retrieve(query)
    context_text = "\n\n".join(c.page_content for c in chunks)
    sources = list({c.metadata.get("source", "Unknown") for c in chunks})

    # Ground supplier-specific questions with live risk-table numbers too,
    # since those live in the CSVs, not the policy docs.
    table = load_supplier_table()
    query_lower = query.lower()
    matched = table[table["name"].str.lower().apply(lambda n: n in query_lower or query_lower in n.lower())]
    named_supplier_match = not matched.empty

    if matched.empty:
        # No supplier named directly - the question is likely about a risk
        # level, category, or "which supplier(s)" in general. Fall back to
        # the whole table (only 15 rows) so the LLM has real data to name,
        # optionally narrowed to the risk level mentioned in the query.
        matched = table
        for level in ("low", "medium", "high"):
            if level in query_lower:
                matched = table[table["risk_level"].str.lower() == level]
                break

    fact_lines = []
    for _, row in matched.iterrows():
        fact_lines.append(
            f"{row['name']} ({row['category']}, {row['location']}): risk={row['risk_level']}, "
            f"on_time_rate={row['on_time_delivery_rate']*100:.0f}%, defect_rate={row['defect_rate']*100:.1f}%, "
            f"avg_lead_time={row['avg_lead_time_days']}d, total_orders={int(row['total_orders'])}, "
            f"phone={row['phone']}, address={row.get('address', 'N/A')}"
        )
    # Knowledge-graph facts (products supplied, category/location relationships)
    # for a directly-named supplier, if Neo4j is reachable.
    graph_fact_lines = []
    if named_supplier_match:
        from backend.supplywise_graph import get_supplier_graph_facts
        for _, row in matched.iterrows():
            seen = set()
            for f in get_supplier_graph_facts(row["name"]):
                if f.get("relationship") == "SUPPLIES" and f["target_name"] not in seen:
                    seen.add(f["target_name"])
                    graph_fact_lines.append(f"{row['name']} SUPPLIES {f['target_name']}")
    graph_fact_text = "\n".join(graph_fact_lines)

    fact_text = "\n".join(fact_lines)

    try:
        from langchain_ollama import ChatOllama
        base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        model = os.getenv("OLLAMA_MODEL", "llama3")
        llm = ChatOllama(base_url=base_url, model=model, temperature=0.1, timeout=60.0, num_predict=400)

        system_instr = (
            "You are SupplyWise, a procurement and supplier intelligence assistant.\n"
            "Answer ONLY using the supplier data and policy context provided below.\n"
            "If the context does not contain the answer, say you don't have that information.\n"
            "Be concise and cite supplier names/numbers directly from the context when relevant.\n"
            "If a phone number or address is present in the Supplier Data for a supplier the user "
            "asks about, always include it directly in your answer - do not withhold contact details "
            "that are present in the context."
        )
        user_msg = (
            f"Supplier Data:\n{fact_text}\n\n"
            f"Knowledge Graph Facts:\n{graph_fact_text or '(none)'}\n\n"
            f"Policy/Document Context:\n{context_text}\n\nQuestion: {query}"
        )
        response = llm.invoke([("system", system_instr), ("human", user_msg)])
        answer = response.content
    except Exception as e:
        logger.warning(f"Ollama unavailable, falling back to context echo: {e}")
        answer = "Ollama is unavailable, so here is the most relevant retrieved information:\n\n"
        answer += fact_text + "\n\n" + (context_text[:500] if context_text else "No matching documents found.")

    return {"answer": answer, "sources": sources, "facts": fact_lines, "graph_facts": graph_fact_lines}


def get_all_suppliers_with_risk():
    """
    Get all suppliers with their risk assessment data
    Returns list of supplier dictionaries with full details
    """
    global _CACHED_SUPPLIER_TABLE
    
    # Load supplier data if not cached
    if _CACHED_SUPPLIER_TABLE is None:
        if not os.path.exists(SUPPLIERS_CSV):
            return []
        _CACHED_SUPPLIER_TABLE = pd.read_csv(SUPPLIERS_CSV)
    
    suppliers_list = []
    for _, row in _CACHED_SUPPLIER_TABLE.iterrows():
        # Get on-time rate (convert from 0-1 to 0-100 if needed)
        on_time_rate = float(row['on_time_delivery_rate'])
        if on_time_rate <= 1.0:
            on_time_rate = on_time_rate * 100
        
        # Get defect rate
        defect_rate = float(row['defect_rate'])
        if defect_rate <= 1.0:
            defect_rate = defect_rate * 100
        
        # Calculate risk level
        risk_level = "Low"
        if on_time_rate < 75 or defect_rate > 6:
            risk_level = "High"
        elif on_time_rate < 90 or defect_rate > 2:
            risk_level = "Medium"
        
        supplier_data = {
            'name': row['name'],
            'category': row['category'],
            'location': row['location'],
            'phone': str(row.get('phone', '')),
            'address': str(row.get('address', '')),
            'website': str(row.get('website', '')),
            'on_time_rate': on_time_rate,
            'defect_rate': defect_rate,
            'avg_lead_time': float(row['avg_lead_time_days']),
            'total_orders': 0,  # Not in CSV, would come from orders.csv join
            'risk_level': risk_level,
            'avg_order_value': 0  # Not in CSV
        }
        suppliers_list.append(supplier_data)
    
    return suppliers_list
