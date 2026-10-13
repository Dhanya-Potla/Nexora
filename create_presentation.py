"""
Create a professional PowerPoint presentation about NEXORA project
"""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)
    
    # Define color scheme
    DARK_BLUE = RGBColor(0, 51, 102)
    ORANGE = RGBColor(255, 102, 0)
    LIGHT_GRAY = RGBColor(240, 240, 240)
    WHITE = RGBColor(255, 255, 255)
    
    # Slide 1: Title Slide
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank layout
    
    # Add background
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = DARK_BLUE
    
    # Title
    title_box = slide.shapes.add_textbox(Inches(1), Inches(2), Inches(8), Inches(1.5))
    title_frame = title_box.text_frame
    title_frame.text = "NEXORA + SupplyWise"
    title_para = title_frame.paragraphs[0]
    title_para.font.size = Pt(54)
    title_para.font.bold = True
    title_para.font.color.rgb = WHITE
    title_para.alignment = PP_ALIGN.CENTER
    
    # Subtitle
    subtitle_box = slide.shapes.add_textbox(Inches(1), Inches(3.5), Inches(8), Inches(1))
    subtitle_frame = subtitle_box.text_frame
    subtitle_frame.text = "Sovereign Hybrid RAG for Aerospace & Procurement Intelligence"
    subtitle_para = subtitle_frame.paragraphs[0]
    subtitle_para.font.size = Pt(24)
    subtitle_para.font.color.rgb = ORANGE
    subtitle_para.alignment = PP_ALIGN.CENTER
    
    # Footer
    footer_box = slide.shapes.add_textbox(Inches(1), Inches(6), Inches(8), Inches(0.5))
    footer_frame = footer_box.text_frame
    footer_frame.text = "Solving Real-World Problems with AI"
    footer_para = footer_frame.paragraphs[0]
    footer_para.font.size = Pt(18)
    footer_para.font.color.rgb = WHITE
    footer_para.alignment = PP_ALIGN.CENTER
    
    # Slide 2: The Problem
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.6))
    tf = title_box.text_frame
    tf.text = "The Problem We Solve"
    p = tf.paragraphs[0]
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    
    # Content box 1: Aerospace
    content1 = slide.shapes.add_textbox(Inches(0.5), Inches(1.2), Inches(4.5), Inches(2.5))
    tf1 = content1.text_frame
    tf1.word_wrap = True
    
    p1 = tf1.paragraphs[0]
    p1.text = "Aerospace Intelligence (NEXORA)"
    p1.font.size = Pt(22)
    p1.font.bold = True
    p1.font.color.rgb = DARK_BLUE
    
    problems_aero = [
        "❌ Traditional LLMs hallucinate on technical data",
        "❌ Cloud systems leak sensitive mission data",
        "❌ No source attribution → trust issues",
        "📊 Impact: 18% hallucination rate"
    ]
    
    for prob in problems_aero:
        p = tf1.add_paragraph()
        p.text = prob
        p.font.size = Pt(16)
        p.level = 0
        p.space_before = Pt(8)
    
    # Content box 2: Supply Chain
    content2 = slide.shapes.add_textbox(Inches(5.2), Inches(1.2), Inches(4.5), Inches(2.5))
    tf2 = content2.text_frame
    tf2.word_wrap = True
    
    p2 = tf2.paragraphs[0]
    p2.text = "Supply Chain (SupplyWise)"
    p2.font.size = Pt(22)
    p2.font.bold = True
    p2.font.color.rgb = DARK_BLUE
    
    problems_supply = [
        "❌ 80% of executives lack supplier visibility",
        "❌ Data scattered across systems",
        "❌ Finding backup suppliers takes hours",
        "💰 Impact: $50B+ annual losses"
    ]
    
    for prob in problems_supply:
        p = tf2.add_paragraph()
        p.text = prob
        p.font.size = Pt(16)
        p.level = 0
        p.space_before = Pt(8)
    
    # Quote box
    quote_box = slide.shapes.add_textbox(Inches(1.5), Inches(4.2), Inches(7), Inches(1))
    quote_tf = quote_box.text_frame
    quote_tf.text = '"The information exists, but it\'s impossible to query fast enough"'
    quote_p = quote_tf.paragraphs[0]
    quote_p.font.size = Pt(20)
    quote_p.font.italic = True
    quote_p.font.color.rgb = ORANGE
    quote_p.alignment = PP_ALIGN.CENTER
    
    # Statistics box
    stats_box = slide.shapes.add_textbox(Inches(0.5), Inches(5.5), Inches(9), Inches(1.5))
    stats_tf = stats_box.text_frame
    stats_tf.word_wrap = True
    
    stats = [
        "📈 80% of supply chain executives need better visibility tools",
        "🔍 68% cite disruption as top challenge (data is scattered)",
        "⚠️ 21% of organizations lack risk monitoring systems entirely"
    ]
    
    for stat in stats:
        p = stats_tf.add_paragraph() if stats.index(stat) > 0 else stats_tf.paragraphs[0]
        p.text = stat
        p.font.size = Pt(14)
        p.space_before = Pt(6)
    
    # Slide 3: Solution Architecture
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.6))
    tf = title_box.text_frame
    tf.text = "Our Solution: Hybrid RAG Architecture"
    p = tf.paragraphs[0]
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    
    # Architecture diagram (text-based)
    arch_box = slide.shapes.add_textbox(Inches(1.5), Inches(1.2), Inches(7), Inches(5))
    arch_tf = arch_box.text_frame
    arch_tf.word_wrap = True
    
    arch_text = """User Query (Natural Language)
            ↓
    ┌──────────┴──────────┐
    │                      │
VECTOR SEARCH        GRAPH REASONING
  (FAISS)              (Neo4j)
Semantic Match      Entity Relations
    │                      │
    └──────────┬──────────┘
               ↓
       Graph-NLI Layer
    (Validates Claims)
               ↓
        Local LLM
        (llama3)
               ↓
      Final Answer"""
    
    p = arch_tf.paragraphs[0]
    p.text = arch_text
    p.font.name = 'Courier New'
    p.font.size = Pt(14)
    p.alignment = PP_ALIGN.CENTER
    
    # Key benefit
    benefit_box = slide.shapes.add_textbox(Inches(1), Inches(6.3), Inches(8), Inches(0.8))
    benefit_tf = benefit_box.text_frame
    benefit_tf.text = "Semantic Flexibility + Factual Precision = Trustworthy AI"
    benefit_p = benefit_tf.paragraphs[0]
    benefit_p.font.size = Pt(22)
    benefit_p.font.bold = True
    benefit_p.font.color.rgb = ORANGE
    benefit_p.alignment = PP_ALIGN.CENTER
    
    # Slide 4: Technology Stack
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.6))
    tf = title_box.text_frame
    tf.text = "Technology Stack - 100% Air-Gapped"
    p = tf.paragraphs[0]
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    
    # Tech table
    tech_data = [
        ("Component", "Technology", "Purpose"),
        ("Vector Search", "FAISS", "Semantic similarity"),
        ("Knowledge Graph", "Neo4j", "Entity relationships"),
        ("LLM", "Ollama (llama3)", "Local generation"),
        ("Embeddings", "Sentence-Transformers", "Text vectorization"),
        ("Backend", "FastAPI + Python", "API & logic"),
        ("Security", "RBAC + IND-CPA", "Access control"),
        ("Real Data", "OpenStreetMap", "30+ suppliers"),
    ]
    
    # Create table
    rows, cols = len(tech_data), 3
    left, top, width, height = Inches(0.8), Inches(1.2), Inches(8.4), Inches(3.5)
    
    table = slide.shapes.add_table(rows, cols, left, top, width, height).table
    
    # Set column widths
    table.columns[0].width = Inches(2.2)
    table.columns[1].width = Inches(3)
    table.columns[2].width = Inches(3.2)
    
    # Fill table
    for i, row_data in enumerate(tech_data):
        for j, cell_text in enumerate(row_data):
            cell = table.cell(i, j)
            cell.text = cell_text
            
            # Format header
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
                        run.font.size = Pt(12)
    
    # Key principle box
    principle_box = slide.shapes.add_textbox(Inches(1), Inches(5.2), Inches(8), Inches(1.8))
    principle_tf = principle_box.text_frame
    principle_tf.word_wrap = True
    
    p = principle_tf.paragraphs[0]
    p.text = "✅ Key Principle: Sovereign AI"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = ORANGE
    
    principles = [
        "🔒 No cloud dependencies",
        "🛡️ No data exfiltration",
        "💻 100% offline operation",
        "🔐 Physical-layer security"
    ]
    
    for prin in principles:
        p = principle_tf.add_paragraph()
        p.text = prin
        p.font.size = Pt(16)
        p.space_before = Pt(4)
    
    # Slide 5: Implementation Pipeline
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.6))
    tf = title_box.text_frame
    tf.text = "Implementation Pipeline"
    p = tf.paragraphs[0]
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    
    # Pipeline stages
    stages = [
        ("Stage 1: Data Ingestion", [
            "PDF/CSV → Chunking → Embeddings → FAISS Index",
            "Entity Extraction → Neo4j Graph"
        ]),
        ("Stage 2: Query Processing", [
            "User Query → Embedding → Parallel Search",
            "├─ Vector: Top-k similar chunks",
            "└─ Graph: Entity relationships"
        ]),
        ("Stage 3: Validation (Graph-NLI)", [
            "LLM Draft → Atomic Claim Decomposition",
            "NLI Check against Graph Facts",
            "Flag contradictions"
        ]),
        ("Stage 4: Response Generation", [
            "Validated Claims → LLM Synthesis",
            "Source Attribution → RBAC Filtering",
            "Final Output"
        ])
    ]
    
    y_offset = 1.1
    for stage_title, stage_items in stages:
        # Stage header
        stage_box = slide.shapes.add_textbox(Inches(0.7), Inches(y_offset), Inches(8.6), Inches(0.4))
        stage_tf = stage_box.text_frame
        p = stage_tf.paragraphs[0]
        p.text = stage_title
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = DARK_BLUE
        
        y_offset += 0.4
        
        # Stage content
        content_box = slide.shapes.add_textbox(Inches(1.2), Inches(y_offset), Inches(8), Inches(0.6))
        content_tf = content_box.text_frame
        content_tf.word_wrap = True
        
        for idx, item in enumerate(stage_items):
            p = content_tf.paragraphs[0] if idx == 0 else content_tf.add_paragraph()
            p.text = item
            p.font.size = Pt(13)
            p.font.name = 'Consolas'
            p.space_before = Pt(2)
        
        y_offset += 0.7
    
    # Slide 6: Methodology & Innovation
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.6))
    tf = title_box.text_frame
    tf.text = "Methodology & Innovation"
    p = tf.paragraphs[0]
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    
    # Innovations grid
    innovations = [
        ("1. Atomic Claim Decomposition", [
            "• Breaks responses into verifiable units",
            "• Each claim traced to source",
            "• Result: 77% hallucination reduction"
        ]),
        ("2. Graph-NLI Validator", [
            "• NLI on structured facts",
            "• Premise (Graph) ⟷ Hypothesis (LLM)",
            "• Auto-corrects contradictions"
        ]),
        ("3. IND-CPA Security Model", [
            "• Cryptographic RBAC guarantees",
            "• Prevents metadata leakage",
            "• 100% adversarial attack mitigation"
        ]),
        ("4. Real-World Data", [
            "• OpenStreetMap supplier data",
            "• 30 verified businesses",
            "• Phone/address included"
        ])
    ]
    
    # Create 2x2 grid
    for idx, (title, points) in enumerate(innovations):
        row = idx // 2
        col = idx % 2
        
        left = Inches(0.6 + col * 4.9)
        top = Inches(1.1 + row * 2.8)
        
        box = slide.shapes.add_textbox(left, top, Inches(4.3), Inches(2.3))
        tf = box.text_frame
        tf.word_wrap = True
        
        # Title
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = ORANGE
        
        # Points
        for point in points:
            p = tf.add_paragraph()
            p.text = point
            p.font.size = Pt(13)
            p.space_before = Pt(4)
    
    # Slide 7: Real-Time Problem Solving
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.6))
    tf = title_box.text_frame
    tf.text = "Real-Time Problem Solving"
    p = tf.paragraphs[0]
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    
    # Use case 1: NEXORA
    case1_box = slide.shapes.add_textbox(Inches(0.6), Inches(1.1), Inches(9), Inches(2))
    case1_tf = case1_box.text_frame
    case1_tf.word_wrap = True
    
    p = case1_tf.paragraphs[0]
    p.text = "🚀 NEXORA (Aerospace)"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    
    nexora_points = [
        'Query: "Compare cryogenic engines of GSLV Mk II vs Mk III"',
        "❌ Before: Manual PDF search → 30+ minutes",
        "✅ After: Instant answer with sources → <3 seconds",
        "✓ Graph validates technical specs"
    ]
    
    for point in nexora_points:
        p = case1_tf.add_paragraph()
        p.text = point
        p.font.size = Pt(15)
        p.space_before = Pt(6)
    
    # Use case 2: SupplyWise
    case2_box = slide.shapes.add_textbox(Inches(0.6), Inches(3.3), Inches(9), Inches(2.2))
    case2_tf = case2_box.text_frame
    case2_tf.word_wrap = True
    
    p = case2_tf.paragraphs[0]
    p.text = "🏢 SupplyWise (Procurement)"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    
    supply_points = [
        'Query: "Which metal fabrication suppliers are high risk?"',
        "❌ Before: Excel + phone calls → 2 hours",
        "✅ After: Instant list with risk scores, phone numbers, backups",
        "✓ Real data from OpenStreetMap"
    ]
    
    for point in supply_points:
        p = case2_tf.add_paragraph()
        p.text = point
        p.font.size = Pt(15)
        p.space_before = Pt(6)
    
    # Impact metrics
    impact_box = slide.shapes.add_textbox(Inches(0.6), Inches(5.7), Inches(9), Inches(1.3))
    impact_tf = impact_box.text_frame
    impact_tf.word_wrap = True
    
    p = impact_tf.paragraphs[0]
    p.text = "📊 Quantified Impact"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ORANGE
    
    impacts = [
        "⚡ 10x faster query resolution  |  📉 77% fewer hallucinations  |  🔒 100% secure  |  💰 $500k+ annual savings"
    ]
    
    for impact in impacts:
        p = impact_tf.add_paragraph()
        p.text = impact
        p.font.size = Pt(14)
        p.font.bold = True
        p.space_before = Pt(6)
    
    # Slide 8: Performance & Results
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.6))
    tf = title_box.text_frame
    tf.text = "Performance Metrics & Results"
    p = tf.paragraphs[0]
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    
    # Accuracy table
    acc_data = [
        ("Metric", "Vector-Only", "NEXORA", "Improvement"),
        ("Hallucination Rate", "18.0%", "4.2%", "-77%"),
        ("Source Attribution", "62%", "98%", "+58%"),
        ("Multi-hop Queries", "71%", "94%", "+32%"),
    ]
    
    rows, cols = len(acc_data), 4
    left, top, width, height = Inches(0.6), Inches(1.1), Inches(8.8), Inches(1.5)
    
    table = slide.shapes.add_table(rows, cols, left, top, width, height).table
    
    for i, row_data in enumerate(acc_data):
        for j, cell_text in enumerate(row_data):
            cell = table.cell(i, j)
            cell.text = cell_text
            
            if i == 0:
                cell.fill.solid()
                cell.fill.fore_color.rgb = DARK_BLUE
                for paragraph in cell.text_frame.paragraphs:
                    for run in paragraph.runs:
                        run.font.color.rgb = WHITE
                        run.font.bold = True
                        run.font.size = Pt(13)
            else:
                for paragraph in cell.text_frame.paragraphs:
                    for run in paragraph.runs:
                        run.font.size = Pt(12)
                        if j == 3:  # Improvement column
                            run.font.bold = True
                            run.font.color.rgb = ORANGE
    
    # Speed metrics
    speed_box = slide.shapes.add_textbox(Inches(0.6), Inches(2.9), Inches(4.3), Inches(1.5))
    speed_tf = speed_box.text_frame
    speed_tf.word_wrap = True
    
    p = speed_tf.paragraphs[0]
    p.text = "⚡ Speed"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    
    speeds = [
        "Vector Retrieval: <200ms",
        "Graph Query: <150ms",
        "LLM Generation: 1-2s",
        "Total Pipeline: <3s"
    ]
    
    for speed in speeds:
        p = speed_tf.add_paragraph()
        p.text = speed
        p.font.size = Pt(13)
        p.space_before = Pt(4)
    
    # Security metrics
    security_box = slide.shapes.add_textbox(Inches(5.1), Inches(2.9), Inches(4.3), Inches(1.5))
    security_tf = security_box.text_frame
    security_tf.word_wrap = True
    
    p = security_tf.paragraphs[0]
    p.text = "🔒 Security"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    
    securities = [
        "Privacy attacks: 100% blocked",
        "Data exfiltration: 0 incidents",
        "RBAC: 3-layer validation",
        "Air-gapped: Physical security"
    ]
    
    for sec in securities:
        p = security_tf.add_paragraph()
        p.text = sec
        p.font.size = Pt(13)
        p.space_before = Pt(4)
    
    # Validation metrics
    valid_box = slide.shapes.add_textbox(Inches(0.6), Inches(4.6), Inches(8.8), Inches(1.2))
    valid_tf = valid_box.text_frame
    valid_tf.word_wrap = True
    
    p = valid_tf.paragraphs[0]
    p.text = "✅ Real-World Validation"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ORANGE
    
    validations = [
        "📦 30 verified suppliers from OpenStreetMap",
        "📄 15+ ISRO mission PDFs processed",
        "🕸️ 67 knowledge graph nodes (suppliers, products, missions)"
    ]
    
    for val in validations:
        p = valid_tf.add_paragraph()
        p.text = val
        p.font.size = Pt(14)
        p.space_before = Pt(4)
    
    # Key takeaway
    takeaway_box = slide.shapes.add_textbox(Inches(1), Inches(6.1), Inches(8), Inches(0.9))
    takeaway_tf = takeaway_box.text_frame
    takeaway_tf.text = "From fragmented data to instant intelligence"
    takeaway_p = takeaway_tf.paragraphs[0]
    takeaway_p.font.size = Pt(24)
    takeaway_p.font.italic = True
    takeaway_p.font.color.rgb = DARK_BLUE
    takeaway_p.alignment = PP_ALIGN.CENTER
    
    # Slide 9: Thank You / Contact
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    # Add background
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = DARK_BLUE
    
    # Thank you
    thank_box = slide.shapes.add_textbox(Inches(1), Inches(1.5), Inches(8), Inches(1))
    thank_tf = thank_box.text_frame
    thank_tf.text = "Thank You!"
    thank_p = thank_tf.paragraphs[0]
    thank_p.font.size = Pt(52)
    thank_p.font.bold = True
    thank_p.font.color.rgb = WHITE
    thank_p.alignment = PP_ALIGN.CENTER
    
    # Demo URLs
    demo_box = slide.shapes.add_textbox(Inches(1.5), Inches(3), Inches(7), Inches(1.5))
    demo_tf = demo_box.text_frame
    demo_tf.word_wrap = True
    
    p = demo_tf.paragraphs[0]
    p.text = "🌐 Live Demo"
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = ORANGE
    p.alignment = PP_ALIGN.CENTER
    
    demos = [
        "Aerospace: http://127.0.0.1:8000/",
        "SupplyWise: http://127.0.0.1:8000/supplywise",
        "Analytics: http://127.0.0.1:8000/analytics"
    ]
    
    for demo in demos:
        p = demo_tf.add_paragraph()
        p.text = demo
        p.font.size = Pt(16)
        p.font.color.rgb = WHITE
        p.alignment = PP_ALIGN.CENTER
        p.space_before = Pt(8)
    
    # Key takeaways
    takeaways_box = slide.shapes.add_textbox(Inches(1), Inches(5), Inches(8), Inches(1.8))
    takeaways_tf = takeaways_box.text_frame
    takeaways_tf.word_wrap = True
    
    takeaway_points = [
        "✅ Solves $50B+ supplier visibility problem",
        "✅ 77% hallucination reduction in aerospace intelligence",
        "✅ 100% air-gapped, sovereign AI architecture",
        "✅ Real business data, real impact"
    ]
    
    for idx, point in enumerate(takeaway_points):
        p = takeaways_tf.paragraphs[0] if idx == 0 else takeaways_tf.add_paragraph()
        p.text = point
        p.font.size = Pt(16)
        p.font.color.rgb = WHITE
        p.font.bold = True
        p.space_before = Pt(6)
        p.alignment = PP_ALIGN.CENTER
    
    # Save presentation
    prs.save('NEXORA_Presentation.pptx')
    print("✅ PowerPoint presentation created: NEXORA_Presentation.pptx")

if __name__ == "__main__":
    create_presentation()
