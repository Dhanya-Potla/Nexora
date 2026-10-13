"""
Excel Import/Export functionality for SupplyWise
"""
import pandas as pd
import io
from typing import List, Dict
import xlsxwriter
from datetime import datetime

def import_suppliers_from_excel(file_content: bytes) -> List[Dict]:
    """
    Import suppliers from Excel/CSV file
    """
    try:
        # Try reading as Excel first
        df = pd.read_excel(io.BytesIO(file_content))
    except:
        # Fall back to CSV
        df = pd.read_csv(io.BytesIO(file_content))
    
    # Expected columns: name, category, location, phone, address, website
    required_cols = ['name', 'category', 'location']
    
    # Check if required columns exist
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")
    
    # Convert to list of dicts
    suppliers = []
    for _, row in df.iterrows():
        supplier = {
            'name': str(row.get('name', '')).strip(),
            'category': str(row.get('category', '')).strip(),
            'location': str(row.get('location', '')).strip(),
            'phone': str(row.get('phone', '')) if pd.notna(row.get('phone')) else None,
            'address': str(row.get('address', '')) if pd.notna(row.get('address')) else None,
            'website': str(row.get('website', '')) if pd.notna(row.get('website')) else None,
        }
        
        # Skip empty rows
        if supplier['name']:
            suppliers.append(supplier)
    
    return suppliers

def export_suppliers_to_excel(suppliers: List[Dict]) -> bytes:
    """
    Export suppliers to formatted Excel file
    """
    output = io.BytesIO()
    
    # Create workbook
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    worksheet = workbook.add_worksheet('Suppliers')
    
    # Define formats
    header_format = workbook.add_format({
        'bold': True,
        'bg_color': '#003366',
        'font_color': 'white',
        'border': 1,
        'align': 'center',
        'valign': 'vcenter'
    })
    
    high_risk_format = workbook.add_format({
        'bg_color': '#FFEBEE',
        'border': 1
    })
    
    medium_risk_format = workbook.add_format({
        'bg_color': '#FFF3E0',
        'border': 1
    })
    
    low_risk_format = workbook.add_format({
        'bg_color': '#E8F5E9',
        'border': 1
    })
    
    cell_format = workbook.add_format({
        'border': 1,
        'valign': 'vcenter'
    })
    
    # Write headers
    headers = ['Name', 'Category', 'Location', 'Risk Level', 'On-Time %', 'Defect %', 'Phone', 'Address', 'Website']
    for col, header in enumerate(headers):
        worksheet.write(0, col, header, header_format)
    
    # Set column widths
    worksheet.set_column(0, 0, 25)  # Name
    worksheet.set_column(1, 1, 18)  # Category
    worksheet.set_column(2, 2, 15)  # Location
    worksheet.set_column(3, 3, 12)  # Risk
    worksheet.set_column(4, 4, 10)  # On-Time
    worksheet.set_column(5, 5, 10)  # Defect
    worksheet.set_column(6, 6, 18)  # Phone
    worksheet.set_column(7, 7, 30)  # Address
    worksheet.set_column(8, 8, 25)  # Website
    
    # Write data
    for row_idx, supplier in enumerate(suppliers, start=1):
        risk_level = supplier.get('risk_level', 'Medium')
        
        # Choose format based on risk
        if risk_level == 'High':
            row_format = high_risk_format
        elif risk_level == 'Low':
            row_format = low_risk_format
        else:
            row_format = medium_risk_format
        
        worksheet.write(row_idx, 0, supplier.get('name', ''), cell_format)
        worksheet.write(row_idx, 1, supplier.get('category', ''), cell_format)
        worksheet.write(row_idx, 2, supplier.get('location', ''), cell_format)
        worksheet.write(row_idx, 3, risk_level, row_format)
        worksheet.write(row_idx, 4, f"{supplier.get('on_time_rate', 0):.1f}%", cell_format)
        worksheet.write(row_idx, 5, f"{supplier.get('defect_rate', 0):.1f}%", cell_format)
        worksheet.write(row_idx, 6, supplier.get('phone', ''), cell_format)
        worksheet.write(row_idx, 7, supplier.get('address', ''), cell_format)
        worksheet.write(row_idx, 8, supplier.get('website', ''), cell_format)
    
    # Add summary section
    summary_row = len(suppliers) + 3
    worksheet.merge_range(summary_row, 0, summary_row, 2, 'SUMMARY STATISTICS', header_format)
    
    total_suppliers = len(suppliers)
    high_risk = len([s for s in suppliers if s.get('risk_level') == 'High'])
    medium_risk = len([s for s in suppliers if s.get('risk_level') == 'Medium'])
    low_risk = len([s for s in suppliers if s.get('risk_level') == 'Low'])
    avg_on_time = sum(s.get('on_time_rate', 0) for s in suppliers) / total_suppliers if total_suppliers > 0 else 0
    
    worksheet.write(summary_row + 1, 0, 'Total Suppliers:', cell_format)
    worksheet.write(summary_row + 1, 1, total_suppliers, cell_format)
    worksheet.write(summary_row + 2, 0, 'High Risk:', high_risk_format)
    worksheet.write(summary_row + 2, 1, high_risk, high_risk_format)
    worksheet.write(summary_row + 3, 0, 'Medium Risk:', medium_risk_format)
    worksheet.write(summary_row + 3, 1, medium_risk, medium_risk_format)
    worksheet.write(summary_row + 4, 0, 'Low Risk:', low_risk_format)
    worksheet.write(summary_row + 4, 1, low_risk, low_risk_format)
    worksheet.write(summary_row + 5, 0, 'Avg On-Time Rate:', cell_format)
    worksheet.write(summary_row + 5, 1, f"{avg_on_time:.1f}%", cell_format)
    
    workbook.close()
    output.seek(0)
    return output.read()

def generate_excel_template() -> bytes:
    """
    Generate an Excel template for supplier import
    """
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    worksheet = workbook.add_worksheet('Supplier Template')
    
    # Format
    header_format = workbook.add_format({
        'bold': True,
        'bg_color': '#003366',
        'font_color': 'white',
        'border': 1
    })
    
    example_format = workbook.add_format({
        'italic': True,
        'font_color': '#666666',
        'border': 1
    })
    
    # Headers
    headers = ['name', 'category', 'location', 'phone', 'address', 'website']
    for col, header in enumerate(headers):
        worksheet.write(0, col, header, header_format)
    
    # Example row
    examples = [
        'ABC Manufacturing',
        'Metal Fabrication',
        'Bengaluru',
        '+91 80 1234 5678',
        '123 Industrial Area, Phase 2',
        'www.abcmfg.com'
    ]
    
    for col, example in enumerate(examples):
        worksheet.write(1, col, example, example_format)
    
    # Instructions
    worksheet.write(3, 0, 'Instructions:')
    worksheet.write(4, 0, '1. Fill in supplier data starting from row 2')
    worksheet.write(5, 0, '2. Required fields: name, category, location')
    worksheet.write(6, 0, '3. Optional fields: phone, address, website')
    worksheet.write(7, 0, '4. Save and upload this file')
    
    workbook.close()
    output.seek(0)
    return output.read()
