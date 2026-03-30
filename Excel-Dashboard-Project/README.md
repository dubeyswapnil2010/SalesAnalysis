# 📊 Excel Data Analyst Project

A comprehensive guide to building a professional sales analytics dashboard in Microsoft Excel.

---

## 🎯 Project Overview

This project demonstrates a complete end-to-end Excel analytics workflow:

1. **Sample Dataset** - Realistic sales data with intentional data quality issues
2. **Data Cleaning** - Remove duplicates, handle missing values, format columns
3. **Calculated Columns** - Add revenue and profit margin calculations
4. **Excel Formulas** - Learn VLOOKUP, IF, SUMIFS, and more
5. **Pivot Table Analysis** - Multi-dimensional data analysis
6. **Interactive Dashboard** - Professional KPIs, charts, and filters

**Skill Level:** Intermediate Excel  
**Time to Complete:** 2-3 hours  
**Final Output:** Professional Sales Analytics Dashboard

---

## 📁 Project Files

### Core Files
- **sample_sales_data.csv** - Raw sales dataset with intentional data quality issues
- **EXCEL_PROJECT_GUIDE.md** - Comprehensive step-by-step guide (9 phases)
- **EXCEL_FORMULAS_REFERENCE.md** - 30+ ready-to-use formulas
- **DATA_CLEANING_CHECKLIST.md** - Detailed verification checklist
- **generate_sample_data.py** - Python script to generate custom data

---

## 🚀 Quick Start

### Step 1: Import Data
Open **EXCEL_PROJECT_GUIDE.md** → Follow **Part 1**
- Import sample_sales_data.csv into Excel
- Set up raw data sheet

### Step 2: Clean Data
Follow **EXCEL_PROJECT_GUIDE.md** → **Part 2**
- Remove 2 duplicate records
- Handle missing values
- Format date column

### Step 3: Add Calculations
Follow **EXCEL_PROJECT_GUIDE.md** → **Part 3**
- Revenue = Quantity × Price
- Profit % = (Profit ÷ Revenue) × 100

### Step 4: Build Analysis
Follow **EXCEL_PROJECT_GUIDE.md** → **Parts 4-5**
- Add 6 example formulas
- Create 3 Pivot Tables

### Step 5: Create Dashboard
Follow **EXCEL_PROJECT_GUIDE.md** → **Parts 6-8**
- 4 KPI cards
- 3 interactive charts
- 2 slicers (region, category)

---

## 📊 Dataset

**File:** sample_sales_data.csv

**Content:**
- 34-36 sales orders
- Date range: Jan 1 - Mar 30, 2024
- Columns: order_id, order_date, customer_name, region, product_category, product_name, quantity, price, revenue, profit
- Regions: North, South, East, West
- Categories: Electronics, Furniture, Software

**Data Quality Issues (for practice):**
- 2 duplicate records
- 6 missing customer names
- 4 missing product categories
- 3 missing product names
- 8 missing revenue values
- 7 missing profit values

---

## 📋 Guide Breakdown

### EXCEL_PROJECT_GUIDE.md (Main Guide)
Comprehensive 9-part guide with step-by-step instructions:

| Part | Description | Topics |
|------|-----------|--------|
| 1 | Data Import | CSV import, sheet setup |
| 2 | Data Cleaning | Duplicates, nulls, formatting |
| 3 | Calculations | Revenue, Profit %, formulas |
| 4 | Formulas | VLOOKUP, IF, SUMIFS examples |
| 5 | Pivot Tables | 3 tables (region, category, monthly) |
| 6 | Dashboard | KPI cards (4 metrics) |
| 7 | Visualizations | Bar, Pie, Line charts |
| 8 | Slicers | Interactive filters |
| 9 | Best Practices | Tips & optimization |

### EXCEL_FORMULAS_REFERENCE.md (Formula Library)
200+ lines of ready-to-use formulas:

- Calculation Formulas (revenue, profit %)
- Lookup Formulas (VLOOKUP, XLOOKUP)
- Conditional Formulas (IF, AND, OR)
- Aggregation Formulas (SUMIFS, COUNTIFS, SUMPRODUCT)
- Dashboard KPI Formulas
- Text & Date Functions
- Error Handling (IFERROR, IFNA)
- Practice Exercises

### DATA_CLEANING_CHECKLIST.md (Verification Guide)
8 phases with detailed checklists:

- Phase 1: Data Preparation
- Phase 2: Data Cleaning
- Phase 3: Calculated Columns
- Phase 4: Quality Verification
- Phase 5: Analysis Sheets
- Phase 6: Dashboard Creation
- Phase 7: Dashboard Finalization
- Phase 8: Documentation

---

## 🎯 Expected Results

### Sample Dataset Statistics
- Total Records: 34 (after cleaning)
- Total Sales: $21,360
- Total Profit: $4,733
- Average Order Value: $628
- Profit Margin: ~22%

### Regional Breakdown
| Region | Sales | % of Total |
|--------|-------|-----------|
| North  | $4,005 | 19% |
| South  | $7,185 | 34% |
| East   | $5,250 | 25% |
| West   | $4,920 | 23% |

### Category Breakdown
| Category | Sales | % of Total |
|----------|-------|-----------|
| Electronics | ~$9,450 | 44% |
| Furniture | ~$3,300 | 15% |
| Software | ~$8,610 | 40% |

---

## 📊 Dashboard Features

**KPI Cards (Top Section)**
- Total Sales: $21,360
- Total Profit: $4,733
- Total Orders: 34
- Average Order Value: $628

**Charts (Middle Section)**
- Sales by Region (Horizontal Bar Chart)
- Sales by Category (Pie Chart)
- Monthly Sales Trend (Line Chart)

**Interactive Filters (Slicers)**
- Region Slicer: North, South, East, West
- Category Slicer: Electronics, Furniture, Software

---

## 🔧 Requirements

### Software
- Microsoft Excel 2016+ (or Excel 365)
  - XLOOKUP requires Excel 365
  - Other features work in Excel 2016+
- Windows, Mac, or Web Excel supported

### Skills
- Basic Excel knowledge
- Comfort with formulas
- Willingness to learn

### Time
- 2-3 hours for complete project
- 30-45 minutes if already familiar with Excel basics

---

## 🎓 Learning Outcomes

After completing this project, you will master:

**Excel Skills**
- CSV import and preparation
- Data deduplication
- Null value handling
- Date and currency formatting
- Table creation

**Formula Skills**
- Arithmetic formulas
- IF statements (simple & nested)
- VLOOKUP / XLOOKUP
- SUMIFS / COUNTIFS
- SUMPRODUCT
- Error handling

**Analysis Skills**
- Pivot table creation
- Multi-dimensional analysis
- Data aggregation
- KPI calculation
- Trend analysis

**Visualization Skills**
- Chart creation
- Chart customization
- Dashboard design
- Interactive elements
- Professional formatting

---

## 🛠️ Troubleshooting

### CSV Import Issues
**Problem:** Data won't import properly
- Use Data → From Text/CSV (not File → Open)
- Select "Comma" as delimiter
- Set date columns as Date type

### Formula Errors
**Problem:** #REF!, #DIV/0!, #N/A errors
- Check cell references match your data
- Use IFERROR for division by zero
- Verify sheet names in formulas

### Pivot Table Issues
**Problem:** Pivot tables don't update with slicers
- Slicers must be connected to pivot tables
- Check Edit Slicer Connections

### Date Formatting
**Problem:** Dates show as numbers (45309)
- Format as Date (right-click → Format Cells → Date)

---

## 📚 Document Reference

| Document | Purpose | When to Use |
|----------|---------|-------------|
| EXCEL_PROJECT_GUIDE.md | Main instructions | Follow sequentially |
| EXCEL_FORMULAS_REFERENCE.md | Formula syntax | Copy formulas as needed |
| DATA_CLEANING_CHECKLIST.md | Progress tracking | Check off each phase |
| generate_sample_data.py | Generate data | Recreate with variations |

---

## ✅ Success Criteria

You've completed the project when you have:

- ✓ Clean dataset with 34 records (no duplicates)
- ✓ All missing values handled
- ✓ Revenue and Profit % calculated
- ✓ 3 working Pivot Tables
- ✓ Dashboard with 4 KPI metrics
- ✓ 3 interactive charts (Bar, Pie, Line)
- ✓ 2 working slicers (Region, Category)
- ✓ Professional formatting and layout
- ✓ Saved as Sales_Analytics_Dashboard.xlsx

---

## 🚀 Next Steps

After completing the basic project:

**Beginner Enhancements**
- Add conditional formatting
- Create Top 10 customers analysis
- Add product ranking
- Create region comparison charts

**Intermediate Enhancements**
- Add data validation and protect worksheets
- Create named ranges for dynamic formulas
- Build forecast analysis with trend analysis
- Create advanced chart types (waterfall, combo)

**Advanced Enhancements**
- Build multiple dashboards for different departments
- Create dashboard templates for reuse
- Implement real-time data connections (native Excel)
- Design interactive KPI tracking systems

---

## 📞 Support

### Within This Project
1. **EXCEL_PROJECT_GUIDE.md** - Detailed step-by-step instructions
2. **EXCEL_FORMULAS_REFERENCE.md** - Formula syntax and examples
3. **DATA_CLEANING_CHECKLIST.md** - Troubleshooting section

### External Resources
- Microsoft Excel Help: File → Help → Search
- Excel Function Documentation: support.microsoft.com/en-us/excel
- YouTube: Search "Excel [skill name]"

---

## 📝 Project Information

**Version:** 1.0  
**Created:** March 2024  
**Compatibility:** Excel 2016+ (including Office 365)  
**Estimated Duration:** 2-3 hours

---

**Ready to build your Excel dashboard?** Start with EXCEL_PROJECT_GUIDE.md Part 1! 🎉
