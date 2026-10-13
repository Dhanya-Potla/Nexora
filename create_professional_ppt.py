"""
Create a professional, well-formatted PowerPoint presentation about SupplyWise
With proper margins, spacing, and cleaner layout
"""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder_images():
    """Create simple placeholder images for the interface"""
    
    # Create dashboard screenshot placeholder
    img = Image.new('RGB', (1200, 700), color=(245, 245, 250))
    draw = ImageDraw.Draw(img)
    
    # Header
    draw.rectangle([0, 0, 1200, 80], fill=(0, 51, 102))
    
    # Title
    try:
        font_large = ImageFont.truetype("arial.ttf", 40)
        font_medium = ImageFont.truetype("arial.ttf", 24)
        font_small = ImageFont.truetype("arial.ttf", 18)
    except:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    draw.text((50, 25), "SupplyWise Dashboard", fill=(255, 255, 255), font=font_large)
    
    # Stats boxes
    colors = [(46, 125, 50), (255, 152, 0), (211, 47, 47), (25, 118, 210)]
    stats = [
        ("30", "Total Suppliers"),
        ("161", "Total Orders"),
        ("82.2%", "On-Time Rate"),
        ("9.1", "Avg Lead Time")
    ]
    
    for idx, (value, label) in enumerate(stats):
        x = 50 + idx * 280
        y = 120
        draw.rectangle([x, y, x + 250, y + 100], fill=colors[idx], outline=(200, 200, 200))
        draw.text((x + 50, y + 20), value, fill=(255, 255, 255), font=font_large)
        draw.text((x + 30, y + 65), label, fill=(255, 255, 255), font=font_small)
    
    # Risk distribution chart placeholder
    draw.rectangle([50, 260, 550, 580], fill=(255, 255, 255), outline=(200, 200, 200))
    draw.text((150, 280), "Risk Distribution", fill=(0, 0, 0), font=font_medium)
    
    # Draw simple bars
    risk_data = [("Low: 10", 150), ("Medium: 16", 300), ("High: 4", 80)]
    for idx, (label, width) in enumerate(risk_data):
        y = 350 + idx * 60
        draw.rectangle([100, y, 100 + width, y + 40], fill=colors[idx % 3])
        draw.text((110, y + 10), label, fill=(255, 255, 255), font=font_small)
    
    # Category breakdown
    draw.rectangle([600, 260, 1100, 580], fill=(255, 255, 255), outline=(200, 200, 200))
    draw.text((700, 280), "Category Breakdown", fill=(0, 0, 0), font=font_medium)
    
    categories = ["Electronics: 8", "Metal Fab: 7", "Chemicals: 5", "Logistics: 4", "Textiles: 3", "Packaging: 3"]
    for idx, cat in enumerate(categories):
        y = 340 + idx * 35
        draw.text((620, y), f"• {cat}", fill=(0, 0, 0), font=font_small)
    
    img.save('dashboard_screenshot.png')
    print("✓ Created dashboard_screenshot.png")
    
    # Create query interface placeholder
    img2 = Image.new('RGB', (1200, 700), color=(245, 245, 250))
    draw2 = ImageDraw.Draw(img2)
    
    # Header
    draw2.rectangle([0, 0, 1200, 80], fill=(0, 51, 102))
    draw2.text((50, 25), "SupplyWise Query Interface", fill=(255, 255, 255), font=font_large)
    
    # Query box
    draw2.rectangle([100, 150, 1100, 250], fill=(255, 255, 255), outline=(100, 100, 100))
    draw2.text((120, 180), 'Query: "Which suppliers are high risk?"', fill=(0, 0, 0), font=font_medium)
    
    # Response box
    draw2.rectangle([100, 300, 1100, 620], fill=(255, 255, 255), outline=(100, 100, 100))
    draw2.text((120, 320), "Response:", fill=(0, 0, 0), font=font_medium)
    
    response_text = [
        "Based on supplier data, the following are high risk:",
        "",
        "1. MetalWorks Industries",
        "   Risk: High (Defect rate: 8.2%, On-time: 68%)",
        "   Phone: +91 80 2338 1707",
        "   Recommendation: Enable dual sourcing",
        "",
        "2. ChemSupply Co.",
        "   Risk: High (Defect rate: 7.1%, On-time: 71%)",
        "   Phone: +91 80 4161 0910",
        "   Backup: Adishwar India Ltd",
    ]
    
    y_pos = 360
    for line in response_text:
        draw2.text((140, y_pos), line, fill=(0, 0, 0), font=font_small)
        y_pos += 25
    
    img2.save('query_screenshot.png')
    print("✓ Created query_screenshot.png")
    
    # Create architecture diagram
    img3 = Image.new('RGB', (1200, 800), color=(255, 255, 255))
    draw3 = ImageDraw.Draw(img3)
    
    # Title
    draw3.text((400, 30), "Hybrid RAG Architecture", fill=(0, 51, 102), font=font_large)
    
    # Query box
    draw3.rectangle([450, 120, 750, 180], fill=(255, 152, 0))
    draw3.text((500, 140), "User Query", fill=(255, 255, 255), font=font_medium)
    
    # Arrow down
    draw3.line([600, 180, 600, 240], fill=(0, 0, 0), width=3)
    draw3.polygon([(600, 240), (590, 220), (610, 220)], fill=(0, 0, 0))
    
    # Vector and Graph boxes
    draw3.rectangle([200, 260, 450, 380], fill=(46, 125, 50))
    draw3.text([250, 300], "Vector Search", fill=(255, 255, 255), font=font_medium)
    draw3.text([270, 330], "(FAISS)", fill=(255, 255, 255), font=font_small)
    
    draw3.rectangle([750, 260, 1000, 380], fill=(25, 118, 210))
    draw3.text([800, 300], "Knowledge Graph", fill=(255, 255, 255), font=font_medium)
    draw3.text([840, 330], "(Neo4j)", fill=(255, 255, 255), font=font_small)
    
    # Arrows to validation
    draw3.line([325, 380, 500, 450], fill=(0, 0, 0), width=3)
    draw3.line([875, 380, 700, 450], fill=(0, 0, 0), width=3)
    
    # Validation box
    draw3.rectangle([450, 450, 750, 530], fill=(211, 47, 47))
    draw3.text([500, 475], "Graph-NLI", fill=(255, 255, 255), font=font_medium)
    draw3.text([520, 505], "Validation", fill=(255, 255, 255), font=font_small)
    
    # Arrow to LLM
    draw3.line([600, 530, 600, 590], fill=(0, 0, 0), width=3)
    draw3.polygon([(600, 590), (590, 570), (610, 570)], fill=(0, 0, 0))
    
    # LLM box
    draw3.rectangle([450, 600, 750, 680], fill=(156, 39, 176))
    draw3.text([520, 625], "Local LLM", fill=(255, 255, 255), font=font_medium)
    
    # Arrow to answer
    draw3.line([600, 680, 600, 730], fill=(0, 0, 0), width=3)
    draw3.polygon([(600, 730), (590, 710), (610, 710)], fill=(0, 0, 0))
    
    # Answer box
    draw3.rectangle([450, 740, 750, 790], fill=(76, 175, 80))
    draw3.text([530, 755], "Answer", fill=(255, 255, 255), font=font_medium)
    
    img3.save('architecture_diagram.png')
    print("✓ Created architecture_diagram.png")

def create_presentation():
    create_placeholder_images()
    
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)
    
    # Define color scheme
    DARK_BLUE = RGBColor(0, 51, 102)
    ORANGE = RGBColor(255, 102, 0)
    GREEN = RGBColor(46, 125, 50)
    WHITE = RGBColor(255, 255, 255)
    LIGHT_BG = RGBColor(248, 249, 250)
    
    # Slide 1: Title Slide
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = DARK_BLUE
    
    title_box = slide.shapes.add_textbox(Inches(1), Inches(2.5), Inches(8), Inches(1))
    tf = title_box.text_frame
    tf.text = "SupplyWise"
    p = tf.paragraphs[0]
    p.font.size = Pt(66)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER
    
    subtitle_box = slide.shapes.add_textbox(Inches(1), Inches(3.7), Inches(8), Inches(0.7))
    tf = subtitle_box.text_frame
    tf.text = "AI-Powered Procurement Intelligence"
    p = tf.paragraphs[0]
    p.font.size = Pt(30)
    p.font.color.rgb = ORANGE
    p.alignment = PP_ALIGN.CENTER
    
    footer_box = slide.shapes.add_textbox(Inches(2), Inches(5.5), Inches(6), Inches(0.5))
    tf = footer_box.text_frame
    tf.text = "Transforming Supplier Visibility with AI"
    p = tf.paragraphs[0]
    p.font.size = Pt(20)
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER
    
    # Slide 2: The Problem
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    title_box = slide.shapes.add_textbox(Inches(0.7), Inches(0.5), Inches(8.6), Inches(0.7))
    tf = title_box.text_frame
    tf.text = "The Problem: Supplier Visibility Crisis"
    p = tf.paragraphs[0]
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    
    # Problem statement
    problem_box = slide.shapes.add_textbox(Inches(1), Inches(1.4), Inches(8), Inches(0.9))
    tf = problem_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = '"Lack of supplier visibility is the #1 operational problem - ahead of cost and disruption frequency"'
    p.font.size = Pt(18)
    p.font.italic = True
    p.font.color.rgb = ORANGE
    p.alignment = PP_ALIGN.CENTER
    
    # Stats in boxes
    stats = [
        ("80%", "Need better visibility tools", (46, 125, 50)),
        ("68%", "Cite disruption as top challenge", (255, 152, 0)),
        ("21%", "Lack risk monitoring systems", (211, 47, 47))
    ]
    
    for idx, (num, desc, color) in enumerate(stats):
        y = 2.6 + idx * 1.4
        
        # Number box
        num_box = slide.shapes.add_textbox(Inches(1.2), Inches(y), Inches(1.8), Inches(0.9))
        shape = num_box
        fill = shape.fill
        fill.solid()
        fill.fore_color.rgb = RGBColor(*color)
        
        tf = num_box.text_frame
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.text = num
        p.font.size = Pt(44)
        p.font.bold = True
        p.font.color.rgb = WHITE
        p.alignment = PP_ALIGN.CENTER
        
        # Description
        desc_box = slide.shapes.add_textbox(Inches(3.3), Inches(y + 0.15), Inches(5.5), Inches(0.6))
        tf = desc_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = desc
        p.font.size = Pt(20)
        p.font.color.rgb = DARK_BLUE
    
    # Bottom insight
    insight_box = slide.shapes.add_textbox(Inches(1), Inches(6.6), Inches(8), Inches(0.7))
    tf = insight_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "💡 Core Issue: Data exists but is IMPOSSIBLE to query fast enough"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    p.alignment = PP_ALIGN.CENTER
    
    # Slide 3: Solution Overview
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    title_box = slide.shapes.add_textbox(Inches(0.7), Inches(0.5), Inches(8.6), Inches(0.7))
    tf = title_box.text_frame
    tf.text = "The Solution: Natural Language Intelligence"
    p = tf.paragraphs[0]
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    
    features = [
        ("🔍", "Natural Language", "Ask questions in plain English, get instant answers from real data"),
        ("📊", "Explainable Risk", "See WHY a supplier is risky, with exact thresholds and history"),
        ("📞", "Instant Contact", "Phone numbers and addresses included - find and call in one step"),
        ("🎯", "Smart Matching", "AI understands context - finds suppliers even with different terms")
    ]
    
    for idx, (icon, title, desc) in enumerate(features):
        row = idx // 2
        col = idx % 2
        left = Inches(0.8 + col * 4.6)
        top = Inches(1.5 + row * 2.5)
        
        # Icon box
        icon_box = slide.shapes.add_textbox(left, top, Inches(0.8), Inches(0.8))
        tf = icon_box.text_frame
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.text = icon
        p.font.size = Pt(40)
        p.alignment = PP_ALIGN.CENTER
        
        # Content box
        content_box = slide.shapes.add_textbox(left + 0.9, top, Inches(3.5), Inches(2.2))
        tf = content_box.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(20)
        p.font.bold = True
        p.font.color.rgb = ORANGE
        
        p = tf.add_paragraph()
        p.text = desc
        p.font.size = Pt(14)
        p.space_before = Pt(6)
    
    # Slide 4: Architecture with Image
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    title_box = slide.shapes.add_textbox(Inches(0.7), Inches(0.5), Inches(8.6), Inches(0.7))
    tf = title_box.text_frame
    tf.text = "Hybrid RAG Architecture"
    p = tf.paragraphs[0]
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    
    # Add architecture image
    if os.path.exists('architecture_diagram.png'):
        left = Inches(1.5)
        top = Inches(1.5)
        pic = slide.shapes.add_picture('architecture_diagram.png', left, top, width=Inches(7))
    
    # Slide 5: Technology Stack
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    title_box = slide.shapes.add_textbox(Inches(0.7), Inches(0.5), Inches(8.6), Inches(0.7))
    tf = title_box.text_frame
    tf.text = "Enterprise Technology Stack"
    p = tf.paragraphs[0]
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    
    tech_data = [
        ("Component", "Technology", "Purpose"),
        ("Vector Search", "FAISS", "Semantic similarity"),
        ("Knowledge Graph", "Neo4j", "Entity relationships"),
        ("AI Engine", "LLaMA3", "Natural language"),
        ("Backend", "FastAPI", "REST API"),
        ("Risk Model", "Scikit-learn", "ML scoring"),
    ]
    
    rows, cols = len(tech_data), 3
    left, top, width, height = Inches(1), Inches(1.5), Inches(8), Inches(2.5)
    
    table = slide.shapes.add_table(rows, cols, left, top, width, height).table
    table.columns[0].width = Inches(2.3)
    table.columns[1].width = Inches(2.5)
    table.columns[2].width = Inches(3.2)
    
    for i, row_data in enumerate(tech_data):
        for j, cell_text in enumerate(row_data):
            cell = table.cell(i, j)
            cell.text = cell_text
            cell.margin_left = Inches(0.1)
            cell.margin_right = Inches(0.1)
            
            if i == 0:
                cell.fill.solid()
                cell.fill.fore_color.rgb = DARK_BLUE
                for paragraph in cell.text_frame.paragraphs:
                    for run in paragraph.runs:
                        run.font.color.rgb = WHITE
                        run.font.bold = True
                        run.font.size = Pt(14)
            else:
                for paragraph in cell.text_frame.paragraphs:
                    for run in paragraph.runs:
                        run.font.size = Pt(13)
    
    # Key features
    features_box = slide.shapes.add_textbox(Inches(1.2), Inches(4.3), Inches(7.6), Inches(2.7))
    tf = features_box.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = "✅ Key Features"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = ORANGE
    
    features = [
        "100% Self-Hosted - Your data stays in your infrastructure",
        "Real Supplier Data - 30+ verified businesses",
        "Sub-Second Response - Instant answers",
        "Explainable AI - See the reasoning"
    ]
    
    for feat in features:
        p = tf.add_paragraph()
        p.text = f"• {feat}"
        p.font.size = Pt(15)
        p.space_before = Pt(6)
    
    # Slide 6: Dashboard Screenshot
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    title_box = slide.shapes.add_textbox(Inches(0.7), Inches(0.5), Inches(8.6), Inches(0.7))
    tf = title_box.text_frame
    tf.text = "Live Dashboard Interface"
    p = tf.paragraphs[0]
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    
    if os.path.exists('dashboard_screenshot.png'):
        left = Inches(0.8)
        top = Inches(1.4)
        pic = slide.shapes.add_picture('dashboard_screenshot.png', left, top, width=Inches(8.4))
    
    # Slide 7: Query Interface Screenshot
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    title_box = slide.shapes.add_textbox(Inches(0.7), Inches(0.5), Inches(8.6), Inches(0.7))
    tf = title_box.text_frame
    tf.text = "Natural Language Query Interface"
    p = tf.paragraphs[0]
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    
    if os.path.exists('query_screenshot.png'):
        left = Inches(0.8)
        top = Inches(1.4)
        pic = slide.shapes.add_picture('query_screenshot.png', left, top, width=Inches(8.4))
    
    # Slide 8: Before/After Comparison
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    title_box = slide.shapes.add_textbox(Inches(0.7), Inches(0.5), Inches(8.6), Inches(0.7))
    tf = title_box.text_frame
    tf.text = "Real-World Impact"
    p = tf.paragraphs[0]
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    
    # Use case
    case_box = slide.shapes.add_textbox(Inches(1), Inches(1.5), Inches(8), Inches(1.8))
    tf = case_box.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = 'Question: "Which metal fabrication suppliers are high risk?"'
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    
    # Before
    before_box = slide.shapes.add_textbox(Inches(1), Inches(3.5), Inches(3.8), Inches(2.5))
    shape = before_box
    fill = shape.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(255, 235, 238)
    
    tf = before_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "❌ BEFORE"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = RGBColor(211, 47, 47)
    
    before_steps = [
        "1. Open Excel spreadsheet",
        "2. Filter by category",
        "3. Check defect rates",
        "4. Look up phone numbers",
        "5. Cross-reference orders",
        "",
        "⏱️ Time: 2 hours"
    ]
    
    for step in before_steps:
        p = tf.add_paragraph()
        p.text = step
        p.font.size = Pt(13)
        p.space_before = Pt(4)
    
    # After
    after_box = slide.shapes.add_textbox(Inches(5.2), Inches(3.5), Inches(3.8), Inches(2.5))
    shape = after_box
    fill = shape.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(232, 245, 233)
    
    tf = after_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "✅ AFTER"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = GREEN
    
    after_steps = [
        "1. Ask SupplyWise",
        "2. Get instant list with:",
        "   • Risk scores",
        "   • Phone numbers",
        "   • Backup recommendations",
        "",
        "⚡ Time: 3 seconds"
    ]
    
    for step in after_steps:
        p = tf.add_paragraph()
        p.text = step
        p.font.size = Pt(13)
        p.space_before = Pt(4)
    
    # Impact
    impact_box = slide.shapes.add_textbox(Inches(1.5), Inches(6.3), Inches(7), Inches(0.8))
    tf = impact_box.text_frame
    p = tf.paragraphs[0]
    p.text = "💰 Impact: 99.96% time reduction | 240x more queries per day"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ORANGE
    p.alignment = PP_ALIGN.CENTER
    
    # Slide 9: ROI
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    title_box = slide.shapes.add_textbox(Inches(0.7), Inches(0.5), Inches(8.6), Inches(0.7))
    tf = title_box.text_frame
    tf.text = "Business Value & ROI"
    p = tf.paragraphs[0]
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    
    # ROI boxes
    roi_data = [
        ("Time Savings", "150 hrs/week", "15 hrs × 10 officers"),
        ("Cost Savings", "$390K/year", "$7,500/week × 52"),
        ("Risk Reduction", "$200K-300K", "Prevent 2-3 disruptions"),
        ("Total Value", "$590K-690K", "Annual benefit")
    ]
    
    for idx, (label, value, desc) in enumerate(roi_data):
        row = idx // 2
        col = idx % 2
        left = Inches(1 + col * 4.5)
        top = Inches(1.8 + row * 2.3)
        
        box = slide.shapes.add_textbox(left, top, Inches(4), Inches(1.8))
        shape = box
        fill = shape.fill
        fill.solid()
        fill.fore_color.rgb = LIGHT_BG
        
        tf = box.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = label
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = DARK_BLUE
        
        p = tf.add_paragraph()
        p.text = value
        p.font.size = Pt(28)
        p.font.bold = True
        p.font.color.rgb = ORANGE
        p.space_before = Pt(8)
        
        p = tf.add_paragraph()
        p.text = desc
        p.font.size = Pt(13)
        p.space_before = Pt(6)
    
    # Bottom note
    note_box = slide.shapes.add_textbox(Inches(1.5), Inches(6.5), Inches(7), Inches(0.7))
    tf = note_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "📈 Payback Period: 2-3 months  |  🚀 Productivity: 240x increase"
    p.font.size = Pt(16)
    p.font.bold = True
    p.alignment = PP_ALIGN.CENTER
    
    # Slide 10: Thank You
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = DARK_BLUE
    
    thank_box = slide.shapes.add_textbox(Inches(1), Inches(2.2), Inches(8), Inches(1))
    tf = thank_box.text_frame
    tf.text = "Thank You!"
    p = tf.paragraphs[0]
    p.font.size = Pt(60)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER
    
    tagline_box = slide.shapes.add_textbox(Inches(1.5), Inches(3.4), Inches(7), Inches(0.7))
    tf = tagline_box.text_frame
    tf.text = "From Fragmented Data to Instant Intelligence"
    p = tf.paragraphs[0]
    p.font.size = Pt(24)
    p.font.italic = True
    p.font.color.rgb = ORANGE
    p.alignment = PP_ALIGN.CENTER
    
    demo_box = slide.shapes.add_textbox(Inches(1.5), Inches(4.7), Inches(7), Inches(1.5))
    tf = demo_box.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = "🌐 Live Demo: http://127.0.0.1:8000/supplywise"
    p.font.size = Pt(18)
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER
    
    p = tf.add_paragraph()
    p.text = "📊 Analytics: http://127.0.0.1:8000/analytics"
    p.font.size = Pt(18)
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER
    p.space_before = Pt(10)
    
    stats_box = slide.shapes.add_textbox(Inches(1.5), Inches(6.5), Inches(7), Inches(0.7))
    tf = stats_box.text_frame
    tf.text = "💰 $500K+ ROI  |  ⚡ 99.9% faster  |  ✅ 30+ real suppliers  |  🔒 Self-hosted"
    p = tf.paragraphs[0]
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER
    
    prs.save('SupplyWise_Professional.pptx')
    print("\n✅ Professional PowerPoint created: SupplyWise_Professional.pptx")

if __name__ == "__main__":
    from pptx.enum.text import MSO_ANCHOR
    create_presentation()
