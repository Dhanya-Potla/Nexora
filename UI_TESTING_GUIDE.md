# 🧪 UI Testing Guide - SupplyWise Enhanced Interface

## Quick Access
🔗 **Open in Browser**: http://127.0.0.1:8000/supplywise

---

## ✅ Complete Testing Checklist

### Tab 1: Overview (Dashboard)
- [ ] Page loads without errors
- [ ] 4 KPI cards display (Total Suppliers, Orders, Lead Time, On-Time Rate)
- [ ] Risk Distribution donut chart renders
- [ ] Feature Importance bar chart shows
- [ ] Category Performance chart displays
- [ ] Charts are interactive (hover shows values)

**Expected Results:**
- Total Suppliers: ~30
- Charts render in ~1-2 seconds
- All data is color-coded properly

---

### Tab 2: Suppliers & Risk
- [ ] Table shows all suppliers
- [ ] Search box filters by name in real-time
- [ ] Category dropdown filters correctly
- [ ] Risk Level dropdown filters (Low/Medium/High)
- [ ] **NEW**: Location dropdown filters by city
- [ ] **NEW**: Min On-Time % input filters numerically
- [ ] Click row to expand risk reasons
- [ ] Phone numbers are clickable (tel: links)
- [ ] Website links open in new tab
- [ ] Risk badges are color-coded

**Test Scenarios:**

#### Scenario 1: Find High-Risk Electronics Suppliers
```
1. Select Category: "Electronics"
2. Select Risk Level: "High"
3. Expected: Should filter to high-risk electronics suppliers only
```

#### Scenario 2: Find Top Performers in Bengaluru
```
1. Select Location: "Bengaluru"
2. Enter Min On-Time: 90
3. Expected: Only Bengaluru suppliers with ≥90% on-time rate
```

#### Scenario 3: Search Specific Supplier
```
1. Type "Aptronix" in search box
2. Expected: Only Aptronix appears in table
```

---

### Tab 3: Products (NEW!)
- [ ] Product grid displays with images
- [ ] All 15 products load
- [ ] Images render correctly (or show fallback)
- [ ] Search box filters products by name/description
- [ ] Category dropdown filters products
- [ ] Product count updates when filtering
- [ ] Click product card opens modal
- [ ] Modal shows full details
- [ ] Close button dismisses modal
- [ ] Click outside modal closes it

**Test Scenarios:**

#### Scenario 1: Browse Electronics Products
```
1. Select Category: "Electronics"
2. Expected: Should show 3 products (Circuit Boards, LED Panels, Power Supplies)
3. Click any product card
4. Expected: Modal opens with full details
```

#### Scenario 2: Search Products
```
1. Type "steel" in search box
2. Expected: Shows Stainless Steel Sheets
3. Clear search
4. Type "industrial"
5. Expected: Shows multiple products with "industrial" in name/description
```

#### Scenario 3: View Product Details
```
1. Click "Industrial Circuit Boards"
2. Expected: Modal shows:
   - Full-size image
   - Category: Electronics
   - Type: Component
   - Price: ₹2,500 / piece
   - Description
   - Common suppliers list
```

---

### Tab 4: Find Suppliers (Semantic Search)
- [ ] Search input accepts natural language
- [ ] Example chips are clickable
- [ ] Clicking chip populates search
- [ ] Search returns relevant suppliers
- [ ] Match score percentage displays
- [ ] Results show full supplier details
- [ ] Phone links work
- [ ] Website links work

**Test Scenarios:**

#### Scenario 1: Use Example Chip
```
1. Click "low-defect circuit board supplier"
2. Expected: Search runs automatically
3. Expected: Returns electronics suppliers ranked by match score
```

#### Scenario 2: Custom Search
```
1. Type: "reliable packaging supplier with fast delivery"
2. Click Search
3. Expected: Returns packaging/logistics suppliers
4. Expected: Match scores show relevance (80%+)
```

---

### Tab 5: Compare (ENHANCED!)
- [ ] Three dropdowns show all suppliers
- [ ] Third dropdown has "(Optional 3rd)" default
- [ ] Compare button is clickable
- [ ] Can compare 2 suppliers
- [ ] Can compare 3 suppliers
- [ ] Supplier cards display side-by-side
- [ ] **NEW**: Metric comparison cards show
- [ ] **NEW**: Winner badges appear on best values
- [ ] **NEW**: Recommendation box displays at bottom
- [ ] Recommendation shows best overall supplier
- [ ] Win count is accurate

**Test Scenarios:**

#### Scenario 1: Compare 2 Suppliers
```
1. Select Supplier A: "Aptronix"
2. Select Supplier B: "Imagine Store"
3. Click "Compare"
4. Expected: 
   - 2 supplier cards side-by-side
   - Metric cards below showing winners
   - Recommendation box naming best supplier
   - Winner badges on best metrics
```

#### Scenario 2: Compare 3 Suppliers
```
1. Select Supplier A: "Aptronix"
2. Select Supplier B: "Imagine Store"
3. Select Supplier C: "Techno Products"
4. Click "Compare"
5. Expected:
   - 3 supplier cards in grid
   - All metrics compared
   - Clear winner identified
   - Win count (e.g., "3 out of 5 metrics")
```

#### Scenario 3: Check Winner Badges
```
1. Run any comparison
2. Look at metric cards
3. Expected: Each metric shows:
   - Supplier name
   - Metric value
   - "BEST" badge on winner in blue/green
```

---

### Tab 6: Excel Tools (NEW!)
- [ ] Page loads with two sections
- [ ] Export button is clickable
- [ ] Template button is clickable
- [ ] Export downloads Excel file
- [ ] Template downloads Excel file
- [ ] Files have correct names
- [ ] Files open in Excel/LibreOffice
- [ ] Export has color-coded rows
- [ ] Template has example data

**Test Scenarios:**

#### Scenario 1: Download Export
```
1. Click "Download Excel Export"
2. Expected: File downloads (suppliers_export.xlsx)
3. Open file in Excel
4. Expected:
   - All supplier data
   - Color-coded rows:
     * Green = Low risk
     * Orange = Medium risk
     * Red = High risk
   - Summary statistics at bottom
   - Professional formatting
```

#### Scenario 2: Download Template
```
1. Click "Download Template"
2. Expected: File downloads (supplier_template.xlsx)
3. Open file in Excel
4. Expected:
   - Empty template with headers
   - Example data in first row
   - Column instructions
   - Proper formatting
```

---

### Tab 7: Ask AI
- [ ] Input box accepts text
- [ ] Ask button is clickable
- [ ] Enter key submits query
- [ ] Loading state shows while processing
- [ ] Answer displays below input
- [ ] Sources list appears if available
- [ ] Error messages show if query fails

**Test Scenarios:**

#### Scenario 1: Ask About Risk
```
1. Type: "Which suppliers are high risk?"
2. Click Ask or press Enter
3. Expected: AI lists high-risk suppliers with reasons
```

#### Scenario 2: Ask About Specific Supplier
```
1. Type: "What is Aptronix's defect rate?"
2. Click Ask
3. Expected: AI provides specific defect rate percentage
```

---

## 🎨 Visual Checks

### Colors
- [ ] Dark theme is consistent (#0a0a0a background)
- [ ] Text is readable (white on dark)
- [ ] Risk badges are color-coded:
  - [ ] Low = Green (#35c46a)
  - [ ] Medium = Orange (#e2b34a)
  - [ ] High = Red (#e25a4a)
- [ ] Accent color is blue (#4a90e2)
- [ ] Hover states work (cards lift on hover)

### Typography
- [ ] Inter font loads from Google Fonts
- [ ] Headings are bold and clear
- [ ] Body text is readable size (13-14px)
- [ ] Muted text has reduced opacity

### Layout
- [ ] Page is responsive (resize browser)
- [ ] Cards have consistent spacing
- [ ] Grids align properly
- [ ] No horizontal scrolling on desktop
- [ ] Mobile view is usable

---

## 🔧 Technical Checks

### Performance
- [ ] Page loads in < 3 seconds
- [ ] Filters update in real-time (< 200ms)
- [ ] Charts render smoothly
- [ ] Product images load progressively
- [ ] No console errors in DevTools

### Network
Open browser DevTools (F12) → Network tab:
- [ ] All API calls return 200 OK
- [ ] `/supplywise/dashboard` loads dashboard data
- [ ] `/supplywise/products` loads product catalog
- [ ] `/supplywise/filters/options` loads filter data
- [ ] `/supplywise/compare` (POST) returns comparison
- [ ] Excel downloads return proper content-type

### Console
Open browser DevTools (F12) → Console tab:
- [ ] No JavaScript errors
- [ ] No 404 errors for missing resources
- [ ] No CORS errors
- [ ] No mixed content warnings

---

## 🐛 Known Issues & Workarounds

### Issue 1: Neo4j Connection Timeout
**Symptom**: Console shows "Unable to retrieve routing information"  
**Impact**: None - app continues in basic mode  
**Status**: Expected behavior (Neo4j not required)

### Issue 2: Image Loading Delays
**Symptom**: Product images load slowly  
**Impact**: Brief delay before images appear  
**Workaround**: Images use lazy loading, will improve with caching

### Issue 3: Large Excel Export
**Symptom**: Export takes 2-3 seconds with 30+ suppliers  
**Impact**: Brief wait before download starts  
**Status**: Normal for Excel generation

---

## 📊 Test Results Template

Copy and fill this out:

```
Testing Date: _______________
Browser: _______________
Screen Size: _______________

✅ PASSED TESTS:
- Overview Tab: [ ]
- Suppliers Tab: [ ]
- Products Tab: [ ]
- Find Suppliers: [ ]
- Compare Tab: [ ]
- Excel Tools: [ ]
- Ask AI: [ ]

❌ FAILED TESTS:
(List any issues)

💡 NOTES:
(Any observations)

Overall Status: PASS / FAIL
```

---

## 🎯 Critical Path Test (Quick 5-Minute Test)

Run these 5 tests to verify core functionality:

### 1. Dashboard Loads (30 seconds)
- Navigate to /supplywise
- Verify KPIs and charts appear

### 2. Products Work (1 minute)
- Click Products tab
- Verify 15 products show with images
- Click one product card
- Verify modal opens

### 3. Filters Work (1 minute)
- Click Suppliers tab
- Select Category: "Electronics"
- Select Risk: "High"
- Verify table filters

### 4. Compare Works (1.5 minutes)
- Click Compare tab
- Select 2 suppliers
- Click Compare
- Verify winner badges and recommendation box

### 5. Excel Downloads (1 minute)
- Click Excel Tools tab
- Click "Download Excel Export"
- Verify file downloads
- Open in Excel

**If all 5 pass: ✅ Core functionality working**

---

## 🚀 Demo Script (For Presentations)

Use this script to showcase features:

### Opening (30 seconds)
```
"This is SupplyWise - an AI-powered procurement intelligence platform. 
Let me show you the new features we've added."
```

### Demo Flow (5 minutes)

**1. Overview (30s)**
```
"Here's our dashboard showing 30 suppliers across 6 categories.
The risk distribution chart shows we have 4 high-risk suppliers
that need attention."
```

**2. Products (1m)**
```
"We now have a product catalog with 15 items. Let me filter 
by Electronics... here are circuit boards, LED panels, and 
power supplies. Click any card for details and supplier info."
```

**3. Advanced Filters (1m)**
```
"The supplier table now has 5 filters. Let me find 
high-performing electronics suppliers in Bengaluru with 
over 90% on-time delivery... and here they are."
```

**4. Comparison (1.5m)**
```
"Let's compare these three suppliers side-by-side. 
The system analyzes all metrics and shows winners with badges.
At the bottom, AI recommends Aptronix as the best choice,
winning 3 out of 5 metrics."
```

**5. Excel Export (1m)**
```
"For management reports, download everything to Excel with 
one click. The export is color-coded by risk level and 
includes summary statistics."
```

**Closing (30s)**
```
"All of this is backed by real supplier data from OpenStreetMap,
RAG-powered AI for questions, and ML risk scoring. The entire
system is running locally on this machine."
```

---

## ✅ Pre-Demo Checklist

Before presenting:
- [ ] Server is running (Terminal ID: 3)
- [ ] Open http://127.0.0.1:8000/supplywise in browser
- [ ] Close unnecessary tabs
- [ ] Zoom to 100% (Ctrl+0)
- [ ] Open DevTools and check for errors
- [ ] Clear browser cache if needed (Ctrl+Shift+Delete)
- [ ] Test one comparison to verify API works
- [ ] Have Excel/LibreOffice ready to open exports

---

## 📝 Feedback Collection

After testing, note:
- **What worked well**: _______________
- **What needs improvement**: _______________
- **Bugs found**: _______________
- **Feature requests**: _______________
- **Performance issues**: _______________

---

## 🎉 Success Criteria

The UI update is successful if:
- ✅ All 7 tabs load without errors
- ✅ Products catalog displays 15 items with images
- ✅ Multi-supplier comparison works (2-3 suppliers)
- ✅ Winner badges and recommendations appear
- ✅ Excel export downloads and opens correctly
- ✅ All 5 supplier filters work
- ✅ No JavaScript console errors
- ✅ Page is responsive and looks professional

---

**Ready to test? Open the app and start with the Critical Path Test!**

🔗 http://127.0.0.1:8000/supplywise
