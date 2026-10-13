"""
Product catalog data for SupplyWise
"""

PRODUCT_CATALOG = [
    # Electronics
    {
        "id": "ELEC-001",
        "name": "Industrial Circuit Boards",
        "category": "Electronics",
        "type": "Component",
        "avg_price": 2500,
        "currency": "INR",
        "unit": "piece",
        "image_url": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=400",
        "description": "High-quality PCBs for industrial applications",
        "common_suppliers": ["Imagine Store", "Adishwar India Limited"]
    },
    {
        "id": "ELEC-002",
        "name": "LED Display Panels",
        "category": "Electronics",
        "type": "Display",
        "avg_price": 15000,
        "currency": "INR",
        "unit": "unit",
        "image_url": "https://images.unsplash.com/photo-1593508512255-86ab42a8e620?w=400",
        "description": "Commercial grade LED displays",
        "common_suppliers": ["Imagine Store"]
    },
    {
        "id": "ELEC-003",
        "name": "Power Supply Units",
        "category": "Electronics",
        "type": "Component",
        "avg_price": 3500,
        "currency": "INR",
        "unit": "unit",
        "image_url": "https://images.unsplash.com/photo-1601972599748-a1acaa10d80a?w=400",
        "description": "Industrial power supplies 500W-2000W",
        "common_suppliers": ["Adishwar India Limited"]
    },
    
    # Metal Fabrication
    {
        "id": "METAL-001",
        "name": "Stainless Steel Sheets",
        "category": "Metal Fabrication",
        "type": "Raw Material",
        "avg_price": 450,
        "currency": "INR",
        "unit": "kg",
        "image_url": "https://images.unsplash.com/photo-1606329757536-8c53d0ea5b0e?w=400",
        "description": "Grade 304 stainless steel sheets",
        "common_suppliers": ["Techno Products", "Decopark"]
    },
    {
        "id": "METAL-002",
        "name": "Industrial Bearings",
        "category": "Metal Fabrication",
        "type": "Component",
        "avg_price": 850,
        "currency": "INR",
        "unit": "piece",
        "image_url": "https://images.unsplash.com/photo-1581092160562-40aa08e78837?w=400",
        "description": "Heavy-duty industrial bearings",
        "common_suppliers": ["Techno Products"]
    },
    {
        "id": "METAL-003",
        "name": "Aluminum Extrusions",
        "category": "Metal Fabrication",
        "type": "Raw Material",
        "avg_price": 320,
        "currency": "INR",
        "unit": "kg",
        "image_url": "https://images.unsplash.com/photo-1619011482757-a8aa9d2f1f6d?w=400",
        "description": "Custom aluminum profiles",
        "common_suppliers": ["Decopark"]
    },
    
    # Chemicals
    {
        "id": "CHEM-001",
        "name": "Industrial Paint",
        "category": "Chemicals",
        "type": "Coating",
        "avg_price": 650,
        "currency": "INR",
        "unit": "liter",
        "image_url": "https://images.unsplash.com/photo-1589939705384-5185137a7f0f?w=400",
        "description": "Industrial grade paint, various colors",
        "common_suppliers": ["Paint suppliers in database"]
    },
    {
        "id": "CHEM-002",
        "name": "Epoxy Resin",
        "category": "Chemicals",
        "type": "Adhesive",
        "avg_price": 1200,
        "currency": "INR",
        "unit": "kg",
        "image_url": "https://images.unsplash.com/photo-1612198188060-c7c2a3b66eae?w=400",
        "description": "Two-component epoxy adhesive",
        "common_suppliers": ["Chemical suppliers"]
    },
    {
        "id": "CHEM-003",
        "name": "Industrial Lubricants",
        "category": "Chemicals",
        "type": "Lubricant",
        "avg_price": 450,
        "currency": "INR",
        "unit": "liter",
        "image_url": "https://images.unsplash.com/photo-1591434855402-8bcaa0e7e7ef?w=400",
        "description": "High-temperature industrial lubricants",
        "common_suppliers": ["Chemical suppliers"]
    },
    
    # Logistics
    {
        "id": "LOG-001",
        "name": "Packaging Boxes",
        "category": "Logistics",
        "type": "Packaging",
        "avg_price": 25,
        "currency": "INR",
        "unit": "piece",
        "image_url": "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=400",
        "description": "Corrugated cardboard boxes, various sizes",
        "common_suppliers": ["Logistics suppliers"]
    },
    {
        "id": "LOG-002",
        "name": "Pallet Wrap",
        "category": "Logistics",
        "type": "Packaging",
        "avg_price": 180,
        "currency": "INR",
        "unit": "roll",
        "image_url": "https://images.unsplash.com/photo-1584438784894-089d6a62b8fa?w=400",
        "description": "Stretch wrap for pallets",
        "common_suppliers": ["Logistics suppliers"]
    },
    
    # Textiles
    {
        "id": "TEXT-001",
        "name": "Industrial Fabric",
        "category": "Textiles",
        "type": "Raw Material",
        "avg_price": 350,
        "currency": "INR",
        "unit": "meter",
        "image_url": "https://images.unsplash.com/photo-1520006403909-838d6b92c22e?w=400",
        "description": "Heavy-duty industrial fabric",
        "common_suppliers": ["Textile suppliers"]
    },
    {
        "id": "TEXT-002",
        "name": "Safety Uniforms",
        "category": "Textiles",
        "type": "Finished Good",
        "avg_price": 850,
        "currency": "INR",
        "unit": "piece",
        "image_url": "https://images.unsplash.com/photo-1581291518857-4e27b48ff24e?w=400",
        "description": "Industrial safety workwear",
        "common_suppliers": ["Textile suppliers"]
    },
    
    # Packaging
    {
        "id": "PACK-001",
        "name": "Bubble Wrap",
        "category": "Packaging",
        "type": "Protective",
        "avg_price": 120,
        "currency": "INR",
        "unit": "roll",
        "image_url": "https://images.unsplash.com/photo-1607627000458-210e8d2bdb1d?w=400",
        "description": "Protective bubble wrap",
        "common_suppliers": ["Packaging suppliers"]
    },
    {
        "id": "PACK-002",
        "name": "Shipping Labels",
        "category": "Packaging",
        "type": "Stationery",
        "avg_price": 15,
        "currency": "INR",
        "unit": "sheet",
        "image_url": "https://images.unsplash.com/photo-1586769852836-bc069f19e1b6?w=400",
        "description": "Adhesive shipping labels",
        "common_suppliers": ["Stationery suppliers"]
    },
]

def get_all_products():
    """Get all products in catalog"""
    return PRODUCT_CATALOG

def get_products_by_category(category: str):
    """Get products filtered by category"""
    return [p for p in PRODUCT_CATALOG if p['category'] == category]

def get_product_by_id(product_id: str):
    """Get specific product by ID"""
    return next((p for p in PRODUCT_CATALOG if p['id'] == product_id), None)

def search_products(query: str):
    """Search products by name or description"""
    query_lower = query.lower()
    return [
        p for p in PRODUCT_CATALOG 
        if query_lower in p['name'].lower() or query_lower in p['description'].lower()
    ]

def get_product_categories():
    """Get list of unique product categories"""
    return list(set(p['category'] for p in PRODUCT_CATALOG))

def get_products_summary():
    """Get summary statistics about products"""
    categories = {}
    total_avg_value = 0
    
    for product in PRODUCT_CATALOG:
        cat = product['category']
        if cat not in categories:
            categories[cat] = {
                'count': 0,
                'total_value': 0,
                'products': []
            }
        categories[cat]['count'] += 1
        categories[cat]['total_value'] += product['avg_price']
        categories[cat]['products'].append(product['name'])
        total_avg_value += product['avg_price']
    
    return {
        'total_products': len(PRODUCT_CATALOG),
        'categories': categories,
        'avg_product_value': total_avg_value / len(PRODUCT_CATALOG) if PRODUCT_CATALOG else 0
    }
