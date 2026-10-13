"""
Builds the final SupplyWise supplier/order dataset from real OpenStreetMap
vendor records (data/supplywise/real_vendors_raw.json).

Identity + contact info (name, address, phone, website) are REAL, sourced
from OSM. Performance history (defect rate, on-time delivery, orders) is
still modeled - no public dataset tracks per-vendor defect/delivery
performance for arbitrary small businesses, so this is generated the same
way as before, seeded per-supplier so it's stable across rebuilds.
"""
import hashlib
import json
import os
import random

import pandas as pd

DATA_DIR = "data/supplywise"
RAW_PATH = os.path.join(DATA_DIR, "real_vendors_raw.json")
PER_CATEGORY = 5

PRODUCTS = {
    "Electronics": ["PCB Assembly", "Microcontroller Unit", "Power Supply Module", "Sensor Array"],
    "Metal Fabrication": ["Steel Bracket", "Aluminum Housing", "CNC Machined Part", "Welded Frame"],
    "Packaging": ["Corrugated Box", "Shrink Wrap Roll", "Pallet", "Foam Insert"],
    "Chemicals": ["Industrial Adhesive", "Coating Solvent", "Cleaning Agent", "Lubricant"],
    "Logistics": ["Freight Service", "Warehousing Slot", "Last-Mile Delivery", "Cold Chain Transport"],
    "Textiles": ["Protective Fabric", "Insulation Cloth", "Filter Mesh", "Woven Liner"],
}


def _seeded_rng(name: str) -> random.Random:
    seed = int(hashlib.sha256(name.encode()).hexdigest(), 16) % (2**32)
    return random.Random(seed)


def select_suppliers(records):
    by_cat = {}
    for r in records:
        by_cat.setdefault(r["category"], []).append(r)

    chosen = []
    for cat, rows in by_cat.items():
        # prefer records with a website (richer/more real-looking listing) and
        # dedupe identical chain names, then spread across cities.
        seen_names = set()
        deduped = []
        for r in sorted(rows, key=lambda r: (r.get("website") is None, r["name"])):
            if r["name"] in seen_names:
                continue
            seen_names.add(r["name"])
            deduped.append(r)
        chosen.extend(deduped[:PER_CATEGORY])
    return chosen


def generate(seed_records):
    os.makedirs(DATA_DIR, exist_ok=True)
    suppliers = []
    for i, r in enumerate(seed_records, start=1):
        rng = _seeded_rng(r["name"])
        tier = rng.choice(["good", "average", "average", "poor"])
        if tier == "good":
            defect_rate = round(rng.uniform(0.0, 0.02), 3)
            on_time_rate = round(rng.uniform(0.9, 1.0), 2)
            lead_time = rng.randint(3, 8)
        elif tier == "average":
            defect_rate = round(rng.uniform(0.02, 0.06), 3)
            on_time_rate = round(rng.uniform(0.75, 0.9), 2)
            lead_time = rng.randint(7, 14)
        else:
            defect_rate = round(rng.uniform(0.06, 0.15), 3)
            on_time_rate = round(rng.uniform(0.4, 0.75), 2)
            lead_time = rng.randint(12, 25)

        suppliers.append({
            "supplier_id": f"SUP-{i:03d}",
            "name": r["name"],
            "category": r["category"],
            "location": r["location"],
            "address": r.get("address") or f"{r['location']}, India",
            "phone": r["phone"],
            "website": r.get("website") or "",
            "data_source": r["source"],
            "avg_lead_time_days": lead_time,
            "defect_rate": defect_rate,
            "on_time_delivery_rate": on_time_rate,
            "years_active": rng.randint(1, 15),
        })

    suppliers_df = pd.DataFrame(suppliers)
    suppliers_df.to_csv(os.path.join(DATA_DIR, "suppliers.csv"), index=False)

    orders = []
    order_id = 1
    for s in suppliers:
        rng = _seeded_rng(s["name"] + "_orders")
        n_orders = rng.randint(3, 8)
        product_pool = PRODUCTS[s["category"]]
        for _ in range(n_orders):
            base_delay = max(0, int(rng.gauss(0, 3)))
            if s["on_time_delivery_rate"] < 0.75:
                base_delay += rng.randint(2, 10)
            quantity = rng.randint(50, 2000)
            price = round(rng.uniform(500, 50000), 2)
            orders.append({
                "order_id": f"ORD-{order_id:04d}",
                "supplier_id": s["supplier_id"],
                "product": rng.choice(product_pool),
                "quantity": quantity,
                "unit_price_inr": price,
                "delivery_delay_days": base_delay,
                "status": "Delivered" if rng.random() > 0.05 else "Delayed",
            })
            order_id += 1

    orders_df = pd.DataFrame(orders)
    orders_df.to_csv(os.path.join(DATA_DIR, "orders.csv"), index=False)

    print(f"Wrote {len(suppliers_df)} REAL suppliers (from OSM) and {len(orders_df)} modeled orders to {DATA_DIR}/")
    print(suppliers_df[["name", "category", "location", "phone"]].to_string(index=False))


if __name__ == "__main__":
    records = json.load(open(RAW_PATH, encoding="utf-8"))
    seed_records = select_suppliers(records)
    generate(seed_records)
