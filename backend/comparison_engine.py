"""
Supplier Comparison Engine
"""
from typing import List, Dict
import pandas as pd

def compare_suppliers(supplier_data_list: List[Dict]) -> Dict:
    """
    Compare multiple suppliers side-by-side
    Returns comparison data with recommendation
    """
    if not supplier_data_list or len(supplier_data_list) < 2:
        return {"error": "Need at least 2 suppliers to compare"}
    
    comparison = {
        "suppliers": [],
        "metrics": {},
        "recommendation": {},
        "winner_counts": {}
    }
    
    # Metrics to compare
    metrics = [
        ('on_time_rate', 'higher_is_better', 'On-Time Delivery Rate'),
        ('defect_rate', 'lower_is_better', 'Defect Rate'),
        ('avg_lead_time', 'lower_is_better', 'Average Lead Time'),
        ('total_orders', 'higher_is_better', 'Total Orders'),
    ]
    
    # Initialize winner counts
    for supplier in supplier_data_list:
        comparison["winner_counts"][supplier['name']] = 0
    
    # Build comparison data
    for metric_key, comparison_type, metric_label in metrics:
        metric_data = {
            "label": metric_label,
            "type": comparison_type,
            "values": {}
        }
        
        values = []
        for supplier in supplier_data_list:
            value = supplier.get(metric_key, 0)
            metric_data["values"][supplier['name']] = value
            values.append((supplier['name'], value))
        
        # Determine winner for this metric
        if comparison_type == 'higher_is_better':
            winner = max(values, key=lambda x: x[1])
        else:
            winner = min(values, key=lambda x: x[1])
        
        metric_data["winner"] = winner[0]
        comparison["winner_counts"][winner[0]] += 1
        
        comparison["metrics"][metric_key] = metric_data
    
    # Build supplier summaries
    for supplier in supplier_data_list:
        comparison["suppliers"].append({
            "name": supplier['name'],
            "category": supplier.get('category', ''),
            "location": supplier.get('location', ''),
            "risk_level": supplier.get('risk_level', 'Medium'),
            "phone": supplier.get('phone', ''),
            "address": supplier.get('address', ''),
            "on_time_rate": supplier.get('on_time_rate', 0),
            "defect_rate": supplier.get('defect_rate', 0),
            "avg_lead_time": supplier.get('avg_lead_time', 0),
            "total_orders": supplier.get('total_orders', 0),
        })
    
    # Overall recommendation
    best_supplier = max(comparison["winner_counts"].items(), key=lambda x: x[1])
    worst_risk = max(supplier_data_list, key=lambda x: 
        1 if x.get('risk_level') == 'High' else 
        0.5 if x.get('risk_level') == 'Medium' else 0
    )
    
    comparison["recommendation"] = {
        "best_overall": best_supplier[0],
        "wins": best_supplier[1],
        "highest_risk": worst_risk['name'],
        "risk_level": worst_risk.get('risk_level', 'Unknown'),
        "suggestion": generate_recommendation(supplier_data_list, best_supplier[0], worst_risk['name'])
    }
    
    return comparison

def generate_recommendation(suppliers: List[Dict], best: str, highest_risk: str) -> str:
    """
    Generate human-readable recommendation
    """
    best_supplier = next(s for s in suppliers if s['name'] == best)
    
    if best == highest_risk:
        return f"⚠️ {best} performs best overall but has high risk. Consider dual-sourcing."
    
    if best_supplier.get('risk_level') == 'Low':
        return f"✅ {best} is the clear winner with low risk. Recommended for primary sourcing."
    elif best_supplier.get('risk_level') == 'Medium':
        return f"👍 {best} performs best with moderate risk. Monitor performance closely."
    else:
        return f"⚠️ {best} performs best but has high risk. Evaluate alternatives."

def get_cost_comparison(suppliers: List[Dict]) -> Dict:
    """
    Compare costs between suppliers
    """
    if not suppliers:
        return {}
    
    costs = []
    for supplier in suppliers:
        # Calculate estimated annual cost based on orders
        avg_order_value = supplier.get('avg_order_value', 0)
        total_orders = supplier.get('total_orders', 0)
        annual_cost = avg_order_value * total_orders
        
        costs.append({
            "name": supplier['name'],
            "annual_cost": annual_cost,
            "avg_order_value": avg_order_value,
            "total_orders": total_orders
        })
    
    # Find cheapest and most expensive
    if costs:
        cheapest = min(costs, key=lambda x: x['annual_cost'])
        most_expensive = max(costs, key=lambda x: x['annual_cost'])
        
        savings = most_expensive['annual_cost'] - cheapest['annual_cost']
        
        return {
            "costs": costs,
            "cheapest": cheapest['name'],
            "most_expensive": most_expensive['name'],
            "potential_savings": savings,
            "savings_percentage": (savings / most_expensive['annual_cost'] * 100) if most_expensive['annual_cost'] > 0 else 0
        }
    
    return {"costs": costs}
