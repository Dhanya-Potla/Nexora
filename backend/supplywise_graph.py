"""
Supplier/Product/Order knowledge graph for SupplyWise, built on the same
Neo4j GraphStore the aerospace pipeline already uses. Populates
Supplier -[:BELONGS_TO]-> Category, Supplier -[:LOCATED_IN]-> Location, and
Supplier -[:SUPPLIES]-> Product relationships from the supplier/order CSVs -
PRD requirement 6 ("Knowledge Graph": represent relationships among
suppliers, products, orders, clients, categories).
"""
import logging

import pandas as pd

from backend.graph_store import GraphStore
from backend.supplywise_pipeline import load_supplier_table, ORDERS_CSV

logger = logging.getLogger(__name__)


def populate_graph():
    table = load_supplier_table()
    orders = pd.read_csv(ORDERS_CSV)

    graph = GraphStore()
    try:
        for _, row in table.iterrows():
            graph.add_entity("Supplier", {
                "name": row["name"],
                "risk_level": row["risk_level"],
                "defect_rate": float(row["defect_rate"]),
                "on_time_delivery_rate": float(row["on_time_delivery_rate"]),
                "phone": row["phone"],
                "address": row.get("address") or "",
            })
            graph.add_entity("Category", {"name": row["category"]})
            graph.add_entity("Location", {"name": row["location"]})
            graph.add_relationship("Supplier", row["name"], "Category", row["category"], "BELONGS_TO")
            graph.add_relationship("Supplier", row["name"], "Location", row["location"], "LOCATED_IN")

        supplier_lookup = table.set_index("supplier_id")["name"].to_dict()
        products_seen = set()
        for _, o in orders.iterrows():
            supplier_name = supplier_lookup.get(o["supplier_id"])
            if not supplier_name:
                continue
            product = o["product"]
            if product not in products_seen:
                graph.add_entity("Product", {"name": product})
                products_seen.add(product)
            graph.add_relationship("Supplier", supplier_name, "Product", product, "SUPPLIES")

        count = graph.count_nodes()
        logger.info(f"SupplyWise graph populated: {count} total nodes")
        return count
    finally:
        graph.close()


def get_supplier_graph_facts(supplier_name: str) -> list:
    """2-hop facts about a supplier (category, location, products supplied)."""
    try:
        graph = GraphStore()
        facts = graph.query_facts(supplier_name)
        graph.close()
        return facts
    except Exception as e:
        logger.warning(f"SupplyWise graph query failed: {e}")
        return []


if __name__ == "__main__":
    n = populate_graph()
    print(f"Populated SupplyWise knowledge graph: {n} nodes")
