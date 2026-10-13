"""
Pulls REAL, verifiable supplier/vendor records from OpenStreetMap (Overpass API)
to replace the synthetic supplier roster - real business names, addresses, and
phone numbers where publicly listed, for the same procurement categories and
cities the SupplyWise demo already uses.

OSM data is open (ODbL) and queryable with no auth/API key. Coverage of phone
numbers on individual businesses varies by city/category - this script keeps
only records that have a genuine phone number, so anything in the final CSV
is a real, contactable business, not a filled-in placeholder.

Performance/risk metrics (defect rate, on-time %) are NOT available from any
public source for arbitrary businesses - no open dataset tracks that. Those
stay model-estimated from order history, same as before. The identity and
contact info are now the real part.
"""
import json
import time
import requests

OVERPASS_URL = "https://overpass-api.de/api/interpreter"
HEADERS = {"User-Agent": "SupplyWiseResearch/1.0 (capstone project, non-commercial)"}

# Approximate bounding boxes (south, west, north, east) for the cities already
# used in the demo dataset.
CITIES = {
    "Bengaluru": (12.85, 77.45, 13.10, 77.75),
    "Chennai": (12.95, 80.15, 13.20, 80.30),
    "Pune": (18.45, 73.75, 18.65, 73.95),
    "Hyderabad": (17.30, 78.30, 17.55, 78.60),
    "Ahmedabad": (22.95, 72.50, 23.10, 72.65),
    "Coimbatore": (10.95, 76.90, 11.10, 77.05),
    "Delhi NCR": (28.45, 76.95, 28.75, 77.35),
}

# category -> OSM tag matchers. Chosen as the closest real-world proxy for
# each procurement category (exact B2B/wholesale tagging is sparse in OSM).
# Deliberately narrow: earlier passes included shop=chemist (pharmacies),
# shop=car_repair (auto mechanics), and shop=doityourself/bag (general
# retail/luggage) as proxies for Chemicals/Logistics/Metal Fabrication/
# Packaging - those are real businesses but the WRONG category, which would
# mislabel a pharmacy as an industrial chemical supplier. Dropped in favor of
# fewer but correctly-categorized matches.
CATEGORY_TAGS = {
    "Electronics": [("shop", "electronics"), ("shop", "electrical")],
    "Metal Fabrication": [("shop", "hardware"), ("craft", "blacksmith"), ("craft", "metal_construction")],
    "Packaging": [("shop", "stationery"), ("shop", "packaging")],
    "Chemicals": [("shop", "paint")],
    "Logistics": [("office", "logistics"), ("office", "courier"), ("amenity", "cargo_center")],
    "Textiles": [("shop", "fabric"), ("shop", "textiles")],
}


def query_city(bbox):
    south, west, north, east = bbox
    clauses = []
    for tags in CATEGORY_TAGS.values():
        for key, val in tags:
            clauses.append(f'node["{key}"="{val}"]({south},{west},{north},{east});')
    query = "[out:json][timeout:60];(" + "".join(clauses) + ");out body;"
    resp = requests.post(OVERPASS_URL, data={"data": query}, headers=HEADERS, timeout=90)
    resp.raise_for_status()
    return resp.json().get("elements", [])


def classify(tags):
    for category, matchers in CATEGORY_TAGS.items():
        for key, val in matchers:
            if tags.get(key) == val:
                return category
    return None


def extract_phone(tags):
    for key in ("phone", "contact:phone", "mobile", "contact:mobile"):
        if tags.get(key):
            return tags[key]
    return None


def main():
    all_records = []
    for city, bbox in CITIES.items():
        print(f"Querying {city}...")
        try:
            elements = query_city(bbox)
        except Exception as e:
            print(f"  failed: {e}")
            continue

        for el in elements:
            tags = el.get("tags", {})
            name = tags.get("name")
            phone = extract_phone(tags)
            if not name or not phone:
                continue  # only keep real, contactable businesses
            category = classify(tags)
            if not category:
                continue
            address_parts = [tags.get(k) for k in ("addr:housenumber", "addr:street", "addr:suburb") if tags.get(k)]
            all_records.append({
                "name": name,
                "category": category,
                "location": city,
                "address": ", ".join(address_parts) if address_parts else None,
                "phone": phone,
                "website": tags.get("website") or tags.get("contact:website"),
                "osm_id": el.get("id"),
                "source": "OpenStreetMap (openstreetmap.org), ODbL",
            })
        time.sleep(1)  # be polite to the shared public Overpass instance

    print(f"\nTotal real businesses found with phone numbers: {len(all_records)}")
    with open("data/supplywise/real_vendors_raw.json", "w", encoding="utf-8") as f:
        json.dump(all_records, f, indent=2, ensure_ascii=False)

    from collections import Counter
    print(Counter(r["category"] for r in all_records))


if __name__ == "__main__":
    main()
