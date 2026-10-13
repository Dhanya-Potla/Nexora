# Data Sourcing & Methodology

## Supplier Identity and Contact Data
Supplier name, category, city, address, phone number, and website in this system are real,
verifiable business records sourced from OpenStreetMap (openstreetmap.org), an open-licensed
(ODbL) public map database. Every supplier listed here is a real, contactable business - not a
synthetic placeholder. Records were filtered to keep only businesses with a publicly listed
phone number, and manually checked so that each business's OSM category genuinely matches its
SupplyWise procurement category (e.g. courier/logistics companies for Logistics, paint/coatings
retailers for Chemicals, industrial bearings and tool suppliers for Metal Fabrication).

## Performance and Risk Data
No public dataset tracks defect rates, on-time delivery percentages, or order history for
arbitrary small businesses - that data is proprietary to whoever actually transacts with a
supplier. Performance metrics (defect rate, on-time delivery rate, average lead time, order
history) in this system are therefore modeled, deterministically seeded per supplier so results
are stable across rebuilds. They represent realistic procurement scenarios for demonstration,
not this specific business's actual audited performance record.

## Why This Split Matters
This mirrors how a real deployment would work on day one: a company already knows who its real
vendors are (name, contact info, category) - that's a solved data problem. What's actually hard,
and what SupplyWise's RAG and ML components are built to solve, is turning that vendor list plus
transactional history (orders, deliveries, defects - which SupplyWise would ingest from the
buyer's own ERP/procurement system once integrated) into fast, explainable answers about risk and
sourcing options.
