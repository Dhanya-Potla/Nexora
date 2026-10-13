"""One-off generator for SupplyWise's synthetic demo dataset.
Run directly to (re)write data/supplywise/suppliers.csv and orders.csv.
"""
import os
import random

import pandas as pd

DATA_DIR = "data/supplywise"

PRODUCTS = {
    "Electronics": ["PCB Assembly", "Microcontroller Unit", "Power Supply Module", "Sensor Array"],
    "Metal Fabrication": ["Steel Bracket", "Aluminum Housing", "CNC Machined Part", "Welded Frame"],
    "Packaging": ["Corrugated Box", "Shrink Wrap Roll", "Pallet", "Foam Insert"],
    "Chemicals": ["Industrial Adhesive", "Coating Solvent", "Cleaning Agent", "Lubricant"],
    "Logistics": ["Freight Service", "Warehousing Slot", "Last-Mile Delivery", "Cold Chain Transport"],
    "Textiles": ["Protective Fabric", "Insulation Cloth", "Filter Mesh", "Woven Liner"],
}

# name -> (category, location, tier). Tier and category are pinned per supplier
# (rather than randomly assigned) so they stay consistent with the narrative in
# data/supplywise/docs/*.md - e.g. Vertex Components is called out there as a
# high-quality Electronics supplier, and Metal Fabrication/Chemicals are called
# out as historically higher-risk categories.
SUPPLIER_SPECS = [
    ("Vertex Components", "Electronics", "Bengaluru", "good"),
    ("Anand MetalWorks", "Metal Fabrication", "Pune", "poor"),
    ("BluePack Industries", "Packaging", "Ahmedabad", "average"),
    ("Sundar Chemicals", "Chemicals", "Chennai", "average"),
    ("Rapid Freight Logistics", "Logistics", "Delhi NCR", "good"),
    ("Coimbatore Textile Mills", "Textiles", "Coimbatore", "average"),
    ("Krishna Electronics", "Electronics", "Hyderabad", "good"),
    ("SteelCore Fabricators", "Metal Fabrication", "Pune", "average"),
    ("GreenBox Packaging", "Packaging", "Ahmedabad", "good"),
    ("Prime Solvents Ltd", "Chemicals", "Chennai", "poor"),
    ("Swift Transport Co", "Logistics", "Delhi NCR", "average"),
    ("Nova Circuit Supplies", "Electronics", "Bengaluru", "average"),
    ("Deccan Alloys", "Metal Fabrication", "Hyderabad", "poor"),
    ("Everest Packaging Group", "Packaging", "Ahmedabad", "good"),
    ("Orion Sensor Systems", "Electronics", "Bengaluru", "average"),
]


def generate():
    random.seed(42)
    os.makedirs(DATA_DIR, exist_ok=True)

    suppliers = []
    for i, (name, category, location, tier) in enumerate(SUPPLIER_SPECS, start=1):
        if tier == "good":
            defect_rate = round(random.uniform(0.0, 0.02), 3)
            on_time_rate = round(random.uniform(0.9, 1.0), 2)
            lead_time = random.randint(3, 8)
        elif tier == "average":
            defect_rate = round(random.uniform(0.02, 0.06), 3)
            on_time_rate = round(random.uniform(0.75, 0.9), 2)
            lead_time = random.randint(7, 14)
        else:
            defect_rate = round(random.uniform(0.06, 0.15), 3)
            on_time_rate = round(random.uniform(0.4, 0.75), 2)
            lead_time = random.randint(12, 25)

        suppliers.append({
            "supplier_id": f"SUP-{i:03d}",
            "name": name,
            "category": category,
            "location": location,
            "avg_lead_time_days": lead_time,
            "defect_rate": defect_rate,
            "on_time_delivery_rate": on_time_rate,
            "years_active": random.randint(1, 15),
        })

    suppliers_df = pd.DataFrame(suppliers)
    suppliers_df.to_csv(os.path.join(DATA_DIR, "suppliers.csv"), index=False)

    orders = []
    order_id = 1
    for s in suppliers:
        n_orders = random.randint(3, 8)
        product_pool = PRODUCTS[s["category"]]
        for _ in range(n_orders):
            base_delay = max(0, int(random.gauss(0, 3)))
            # Poor suppliers run later more often.
            if s["on_time_delivery_rate"] < 0.75:
                base_delay += random.randint(2, 10)
            quantity = random.randint(50, 2000)
            price = round(random.uniform(500, 50000), 2)
            orders.append({
                "order_id": f"ORD-{order_id:04d}",
                "supplier_id": s["supplier_id"],
                "product": random.choice(product_pool),
                "quantity": quantity,
                "unit_price_inr": price,
                "delivery_delay_days": base_delay,
                "status": "Delivered" if random.random() > 0.05 else "Delayed",
            })
            order_id += 1

    orders_df = pd.DataFrame(orders)
    orders_df.to_csv(os.path.join(DATA_DIR, "orders.csv"), index=False)

    print(f"Wrote {len(suppliers_df)} suppliers and {len(orders_df)} orders to {DATA_DIR}/")


if __name__ == "__main__":
    generate()
