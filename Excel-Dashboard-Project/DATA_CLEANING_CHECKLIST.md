# Excel Data Cleaning Checklist & Summary

## PROJECT OVERVIEW

This Excel Data Analyst Project demonstrates a complete end-to-end analytics workflow:
- Data Import & Cleaning
- Calculated Columns & Formulas
- Pivot Table Analysis
- Interactive Dashboard Creation

**Expected Time to Complete:** 2-3 hours  
**Excel Skills Level:** Intermediate  
**Files Included:** 4 documents + sample dataset

---

## INCLUDED FILES

### 1. **sample_sales_data.csv**
Raw dataset with:
- 34-36 records (includes duplicates)
- 10 columns (order_id through profit)
- Intentional data quality issues for practice
- Date range: Jan 1 - Mar 30, 2024

**Data Issues Present:**
- ✗ 2 duplicate orders (O005, O014)
- ✗ 6 missing customer names
- ✗ 4 missing product categories
- ✗ 3 missing product names
- ✗ 8 missing revenue values
- ✗ 7 missing profit values

### 2. **EXCEL_PROJECT_GUIDE.md**
Comprehensive 9-part guide including:
- Part 1: Data import steps
- Part 2: Data cleaning procedures
- Part 3: Calculated column setup
- Part 4: Formula examples (VLOOKUP, IF, SUMIFS)
- Part 5: Pivot table creation (3 tables)
- Part 6: Dashboard design with KPIs
- Part 7: Chart creation (Bar, Pie, Line)
- Part 8: Slicer setup for interactivity
- Part 9: Best practices and tips

### 3. **EXCEL_FORMULAS_REFERENCE.md**
Quick reference guide with:
- 30+ ready-to-use formulas
- Formula placement guide
- Error handling techniques
- Keyboard shortcuts
- Practice exercises

### 4. **generate_sample_data.py**
Python script to:
- Generate custom sample datasets
- Adjust missing value rate
- Adjust duplicate rate
- Change number of records
- Export to CSV format

---

## PHASE 1: DATA PREPARATION

### Pre-Import Checklist
- [ ] Excel is closed
- [ ] sample_sales_data.csv is in the project folder
- [ ] Excel is opened (blank workbook)

### Import Process
- [ ] File → Open → Select sample_sales_data.csv
  - OR: Data → From Text/CSV → Select file
- [ ] Text Import Wizard appears
- [ ] **Set delimiter:** Comma ✓
- [ ] **Set data types:** Date columns as Date
- [ ] Click **Load** to import
- [ ] Data appears in Sheet1
- [ ] Rename sheet tab to **"Raw Data"**

**Expected Result:** 34-36 rows + 1 header row

---

## PHASE 2: DATA CLEANING

### Step 1: Remove Duplicates

**Before:** 36 total rows

Process:
- [ ] **Select all data** (Ctrl+A or click corner cell)
- [ ] Go to **Data** tab
- [ ] Click **Remove Duplicates** (or **Data Tools** → **Remove Duplicates**)
- [ ] Ensure **all columns are checked**
- [ ] Click **OK**

**After:** 34 unique rows
**Removed:** 2 duplicate orders (O005, O014)

### Step 2: Handle Missing Customer Names

**Issue:** 6 rows missing customer names (cells show blank)

**Solution Option A: Universal Fill**
- [ ] Click on empty customer_name cell
- [ ] Type: `"Unknown Customer"` or `"Unknown"`
- [ ] Press Enter
- [ ] Fill down to all empty cells (select cells, Ctrl+D)

**Solution Option B: Formula Fill**
- [ ] In first empty cell, enter: `="UNKNOWN_"&A2`
- [ ] Copy down
- [ ] Copy results, then Paste Special → **Values only**

**After:** All customer names filled

### Step 3: Handle Missing Product Categories

**Issue:** 4 rows missing product_category (look at product_name context)

**Solution:**
- [ ] Manually review each missing row
- [ ] Look at product_name to infer category:
  - Laptop/Monitor/Keyboard/Mouse/Printer → "Electronics"
  - Office Chair/Desk/Bookshelf → "Furniture"
  - Microsoft Office/Adobe Suite → "Software"
- [ ] Enter appropriate category

**Reference:**
| Product | Category |
|---------|----------|
| Laptop, Monitor, Keyboard, Mouse, Printer | Electronics |
| Office Chair, Desk, Bookshelf | Furniture |
| Microsoft Office, Adobe Suite | Software |

**After:** All categories filled

### Step 4: Handle Missing Product Names

**Issue:** 3 rows missing product_name

**Solution:**
- [ ] Check nearby rows with same product_name and category context
- [ ] Review if it's a well-known product
- [ ] Fill with most likely product or leave as "Unknown Product"

**After:** Product names filled or marked "Unknown"

### Step 5: Format Date Column

**Current:** Dates may show as numbers (e.g., 45309)

Process:
- [ ] **Select entire order_date column** (Column B)
- [ ] Right-click → **Format Cells** (or Ctrl+1)
- [ ] Go to **Number** tab
- [ ] Select **Date** category
- [ ] Choose format: **3/14/2024** or **2024-03-14**
- [ ] Click **OK**

**After:** All dates display as proper dates

### Step 6: Column Formatting (Optional but Recommended)

- [ ] **Currency columns** (price, revenue, profit):
  - Select columns → Format Cells → Number → Currency ($)
  - Set decimal places: 2
  
- [ ] **Quantity column** (numeric):
  - Format as Number with 0 decimal places

**After:** Professional formatting applied

---

## PHASE 3: ADD CALCULATED COLUMNS

### Step 7: Calculate Revenue (if not already present)

**Formula:** Quantity × Price = Revenue

Process:
- [ ] Click on **Cell I2** (first data row of revenue column)
- [ ] Enter formula: `=F2*G2`
  - Where F = Quantity, G = Price
- [ ] Press **Enter**
- [ ] Select cell I2 (copy it: Ctrl+C)
- [ ] Select range I3:I36 (all remaining rows)
- [ ] Paste: Ctrl+V

**Verify:**
- [ ] All revenue cells show calculations
- [ ] No #DIV/0! or #N/A errors
- [ ] Values appear correct (e.g., 3 × 300 = 900)

### Step 8: Calculate Profit % (new column)

**Formula:** (Profit ÷ Revenue) × 100 = Profit %

Process:
- [ ] Go to **Column J** (or next empty column)
- [ ] In J1, type header: **"Profit %"**
- [ ] In J2, enter formula: `=IF(I2=0, 0, (H2/I2)*100)`
  - IF statement prevents division by zero
  - H = Profit, I = Revenue
- [ ] Press **Enter**
- [ ] Copy J2 and paste to J3:J36

**Format Column J:**
- [ ] Select entire column J (except header)
- [ ] Right-click → **Format Cells**
- [ ] **Number** tab → **Percentage**
- [ ] Set decimal places: 2
- [ ] Click **OK**

**Verify:**
- [ ] All values show as percentages (0.00%)
- [ ] Values make sense (e.g., 20% profit on $900 revenue = $180 profit)

---

## PHASE 4: DATA QUALITY VERIFICATION

### Step 9: Final Data Check

**Completeness Check:**
- [ ] No empty customer_name cells
- [ ] No empty product_category cells
- [ ] No empty product_name cells
- [ ] All revenue cells have values (quantity × price)
- [ ] All profit % cells calculated
- [ ] Row count: 34 unique records

**Consistency Check:**
- [ ] All dates between Jan 1 - Mar 30, 2024
- [ ] All regions are: North, South, East, Or West
- [ ] All categories are: Electronics, Furniture, or Software
- [ ] All quantities are positive numbers
- [ ] All prices are positive numbers
- [ ] Profit % between 0-100% (for most products)

**Accuracy Check:**
- [ ] Spot check revenue: 1 × $1200 = $1200 ✓
- [ ] Spot check revenue: 4 × $45 = $180 ✓
- [ ] Spot check profit %: $120 / $1200 = 10% ✓

**Create First Table Format (Optional):**
- [ ] Select all data including headers
- [ ] Press **Ctrl+T** (Format as Table)
- [ ] Choose table style
- [ ] Benefits: Auto-filtering, consistent formatting

---

## PHASE 5: CREATE ANALYSIS SHEETS

### Step 10: Create Formulas Reference Sheet

- [ ] Right-click sheet tab → **Insert Sheet**
- [ ] Name it: **"Formulas Reference"**
- [ ] Add formula examples from EXCEL_FORMULAS_REFERENCE.md
- [ ] Test each formula

**Formulas to include:**
- [ ] VLOOKUP example
- [ ] XLOOKUP example
- [ ] IF statement (simple and nested)
- [ ] SUMIFS example for by region
- [ ] COUNTIFS example
- [ ] SUMPRODUCT example

### Step 11: Create Pivot Tables

**Pivot Table 1: Sales by Region**
- [ ] Select Raw Data
- [ ] Insert → Pivot Table → New Worksheet
- [ ] Rows: region
- [ ] Values: Sum of revenue, Sum of profit
- [ ] Name sheet: **"Pivot - Region"**

**Expected totals:**
| Region | Revenue | Profit |
|--------|---------|--------|
| North | ~$4,005 | ~$929 |
| South | ~$7,185 | ~$1,635 |
| East | ~$5,250 | ~$1,095 |
| West | ~$4,920 | ~$1,074 |
| **GRAND TOTAL** | **~$21,360** | **~$4,733** |

**Pivot Table 2: Sales by Category**
- [ ] Select Raw Data
- [ ] Insert → Pivot Table → New Worksheet
- [ ] Rows: product_category
- [ ] Values: Sum of revenue, Sum of quantity
- [ ] Name sheet: **"Pivot - Category"**

**Pivot Table 3: Monthly Sales Trend**
- [ ] Select Raw Data
- [ ] Insert → Pivot Table → New Worksheet
- [ ] Rows: order_date (grouped by month)
- [ ] Values: Sum of revenue
- [ ] Name sheet: **"Pivot - Monthly"**

---

## PHASE 6: CREATE DASHBOARD

### Step 12: Create Dashboard Sheet

- [ ] Right-click sheet tab → **Insert Sheet**
- [ ] Name it: **"Dashboard"**
- [ ] Leave blank for layout

### Step 13: Add KPI Cards

**KPI 1: Total Sales (B2)**
- [ ] Click cell B2
- [ ] Type formula: `=SUM('Raw Data'!I:I)`
- [ ] Label in B1: **Total Sales**
- [ ] Format B2:
  - [ ] Font: Bold, Size 28
  - [ ] Number: Currency ($)
  - [ ] Background: Light Blue
  - [ ] Borders: Thick

**KPI 2: Total Profit (D2)**
- [ ] Formula: `=SUM('Raw Data'!H:H)`
- [ ] Label D1: **Total Profit**
- [ ] Format: Bold, Size 28, Currency, Light Green

**KPI 3: Total Orders (F2)**
- [ ] Formula: `=COUNTA('Raw Data'!A:A)-1`
- [ ] Label F1: **Total Orders**
- [ ] Format: Bold, Size 28, Light Orange

**KPI 4: Average Order Value (H2)**
- [ ] Formula: `=AVERAGE('Raw Data'!I:I)`
- [ ] Label H1: **Avg Order Value**
- [ ] Format: Bold, Size 28, Currency

**Expected KPI Values:**
- Total Sales: ~$21,360
- Total Profit: ~$4,733
- Total Orders: 34
- Average Order Value: ~$628

### Step 14: Create Charts

**Chart 1: Sales by Region (Bar Chart)**
- [ ] Use Pivot - Region sheet data
- [ ] Select region data + revenue
- [ ] Insert → Chart → Horizontal Bar Chart
- [ ] Title: "Sales by Region"
- [ ] Copy to Dashboard (under KPIs)

**Chart 2: Sales by Category (Pie Chart)**
- [ ] Use Pivot - Category sheet data
- [ ] Select category + revenue
- [ ] Insert → Chart → Pie Chart
- [ ] Title: "Sales by Category"
- [ ] Display percentages
- [ ] Copy to Dashboard

**Chart 3: Monthly Trend (Line Chart)**
- [ ] Use Pivot - Monthly sheet data
- [ ] Select month + revenue
- [ ] Insert → Chart → Line Chart
- [ ] Title: "Monthly Sales Trend"
- [ ] Add axis labels
- [ ] Copy to Dashboard

### Step 15: Add Slicers

**Slicer 1: Region Filter**
- [ ] Click on Pivot - Region table
- [ ] Insert → Slicer
- [ ] Select "region" field
- [ ] Copy slicer to Dashboard
- [ ] Position below KPIs
- [ ] Style: Professional color scheme

**Slicer 2: Category Filter**
- [ ] Click on Pivot - Category table
- [ ] Insert → Slicer
- [ ] Select "product_category" field
- [ ] Copy slicer to Dashboard
- [ ] Position next to Region slicer

**Test Slicers:**
- [ ] Click "North" in region slicer
- [ ] Verify pivots and charts update
- [ ] Click "Electronics" in category slicer
- [ ] Verify all updates work

---

## PHASE 7: FINALIZE DASHBOARD

### Step 16: Dashboard Formatting

**Colors & Style:**
- [ ] Set background color (light gray or white)
- [ ] Use consistent color scheme:
  - KPIs: Blues, Greens, Oranges
  - Charts: Professional palette
  - Slicers: Matching theme
  
**Layout:**
- [ ] KPI cards: Top row
- [ ] Slicers: Second row
- [ ] Charts: Remaining space (3-column layout)
- [ ] Proper spacing between elements

**Titles & Labels:**
- [ ] Dashboard title: **"SALES ANALYTICS DASHBOARD"**
- [ ] Section headers for chart groups
- [ ] Chart titles visible and legible
- [ ] Font: Calibri or Arial, Size 11

### Step 17: Test Interactivity

- [ ] Click each slicer option
- [ ] Verify pivot tables update
- [ ] Verify charts refresh
- [ ] Verify KPIs remain stable or update as expected
- [ ] Test "Clear Filter" button on slicers

### Step 18: Add Data Validation (Optional)

Create dropdown for future data entry:
- [ ] Select region column in Raw Data
- [ ] Data → Data Validation
- [ ] List → Source: "North, South, East, West"
- [ ] Repeat for product_category

---

## PHASE 8: DOCUMENTATION & CLEANUP

### Step 19: Add Legend Sheet (Optional)

- [ ] Create new sheet: **"Legend"**
- [ ] Document column definitions
- [ ] List all abbreviations
- [ ] Explain calculated column formulas
- [ ] Note data source and date range

### Step 20: Finalize & Save

- [ ] Delete any temporary/practice sheets
- [ ] Arrange sheet tabs in logical order:
  1. Dashboard (primary)
  2. Raw Data
  3. Pivot - Region
  4. Pivot - Category
  5. Pivot - Monthly
  6. Formulas Reference
  7. Legend

**Final Save:**
- [ ] File → Save As
- [ ] Filename: `Sales_Analytics_Dashboard.xlsx`
- [ ] Format: **Excel Workbook (.xlsx)**
- [ ] Location: Project folder

---

## EXPECTED FINAL RESULTS

### Dashboard Metrics Summary

| Metric | Value | Status |
|--------|-------|--------|
| Total Sales Revenue | $21,360 | ✓ |
| Total Profit | $4,733 | ✓ |
| Total Orders | 34 | ✓ |
| Average Order Value | $628 | ✓ |
| Profit Margin | ~22% | ✓ |

### Regional Breakdown
| Region | Sales | % of Total |
|--------|-------|-----------|
| North | $4,005 | 19% |
| South | $7,185 | 34% |
| East | $5,250 | 25% |
| West | $4,920 | 23% |

### Category Breakdown
| Category | Sales | # Orders |
|----------|-------|----------|
| Electronics | ~$9,450 | 14 |
| Furniture | ~$3,300 | 8 |
| Software | ~$8,610 | 12 |

---

## TROUBLESHOOTING GUIDE

### Common Issues

**Issue: "Duplicate records still showing"**
- Solution: Did you remove header row from selection? Reset and try again.

**Issue: Formulas show #REF! error**
- Solution: Delete raw data column references changed. Check sheet names.

**Issue: Charts don't update with slicer**
- Solution: Slicers must be connected to pivot tables. Check slicer connections.

**Issue: "Missing values still present"**
- Solution: Did you fill ALL empty cells? Use Find & Replace (Ctrl+H) to verify blanks.

**Issue: Date column shows numbers (45309)**
- Solution: Format as Date (right-click → Format Cells → Date)

**Issue: Profit %shows as decimal (0.22) instead of 22%**
- Solution: Format as Percentage (right-click → Format Cells → Percentage)

---

## SKILLS DEMONSTRATED

After completing this project, you will have mastered:

✓ **Data Import & Cleaning**
- CSV import into Excel
- Removing duplicates
- Handling missing values
- Data formatting

✓ **Formulas & Calculations**
- Basic arithmetic (×, ÷)
- IF statements (simple & nested)
- VLOOKUP / XLOOKUP
- SUMIFS / COUNTIFS
- Error handling with IFERROR

✓ **Data Analysis**
- Pivot table creation
- Multi-dimensional analysis
- Grouping and aggregation

✓ **Visualization**
- Chart creation (bar, pie, line)
- Chart customization
- Interactive dashboards

✓ **Dashboard Design**
- KPI creation
- Layout optimization
- Interactivity with slicers
- Professional formatting

---

## NEXT STEPS & ENHANCEMENTS

After completing the basic project, try:
- [ ] Add more data (recreate with generate_sample_data.py)
- [ ] Create additional metrics (Top 10 customers, Product ranking)
- [ ] Add conditional formatting (highlight top performers)
- [ ] Create Power Query (Data → From Other Sources)
- [ ] Build SQL queries to refresh data automatically
- [ ] Connect to Power BI for advanced visualizations

---

**Congratulations on creating your first Excel Analytics Dashboard!** 🎉

For questions, refer to:
- EXCEL_PROJECT_GUIDE.md (detailed steps)
- EXCEL_FORMULAS_REFERENCE.md (formula syntax)
- generate_sample_data.py (regenerate data)
