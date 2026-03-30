# Complete Excel Data Analyst Project Guide

## Overview
This project demonstrates a complete Excel-based data analytics workflow including data cleaning, calculations, analysis, and dashboard creation.

---

## PART 1: DATA PREPARATION

### Step 1: Import Sample Data into Excel
1. Open Excel and create a new workbook
2. Go to **Data** → **From Text/CSV**
3. Select `sample_sales_data.csv` from the project folder
4. In the Text Import Wizard:
   - Delimiter: Comma
   - Data type: General (except dates - set as Date)
   - Click **Load**
5. Rename the sheet tab to **"Raw Data"**

### Data Overview
**Columns in the dataset:**
- order_id: Unique order identifier
- order_date: Date of the order
- customer_name: Name of the customer
- region: Sales region (North, South, East, West)
- product_category: Category (Electronics, Furniture, Software)
- product_name: Specific product name
- quantity: Number of units ordered
- price: Unit price
- revenue: Total revenue per order
- profit: Profit from the order

**Data Issues Present:**
- Missing values (blanks) in customer_name, product_category, product_name, revenue, and profit
- Duplicate records (e.g., O005, O014)
- Incomplete calculated columns (revenue, profit)

---

## PART 2: DATA CLEANING

### Step 2: Remove Duplicates
1. **Select all data** → Ctrl+A or click corner cell
2. Go to **Data** → **Remove Duplicates** (or **Data Tools → Remove Duplicates** in some versions)
3. Select all columns to check for duplicates
4. Click **OK**
   - *Expected result: Should remove 2 duplicate rows*
   - Your data should now have approximately 32 unique records

### Step 3: Handle Missing Values

#### For Customer Name (Missing in some rows):
1. Click on first empty customer_name cell
2. Enter a formula: `="Unknown_"&A2` (creates "Unknown_O006")
3. Or manually enter "Unknown Customer"
4. Copy this value down for all missing rows

#### For Product Category & Product Name:
1. Identify rows with missing product information
2. Use VLOOKUP to fill from another row with the same product, or
3. Manually research and fill (suggested: look at context from other orders)

#### For Revenue & Profit:
- These will be recalculated in Step 4, so blanks are acceptable for now

### Step 4: Format Date Column
1. Select the entire **order_date** column (Column B)
2. Right-click → **Format Cells** (or Ctrl+1)
3. Go to **Number** tab
4. Select **Date** category
5. Choose format: **3/14/2024** (or your preferred date format)
6. Click **OK**

### Step 5: Verify Data Quality
After cleaning:
- ✓ No duplicate rows
- ✓ No blank customer names
- ✓ All product categories filled
- ✓ All dates properly formatted
- ✓ Consistent data types

---

## PART 3: CALCULATED COLUMNS

### Step 6: Add Calculated Columns

#### Add Revenue Column (if not calculated)
*Column H already has headers; create formulas in row 2*

1. Click on first empty revenue cell in column I (row 2)
2. Enter formula: `=F2*G2` (quantity × price)
3. Press Enter
4. Select cell I2, copy it (Ctrl+C)
5. Select range I3:I35 (all rows with data)
6. Paste (Ctrl+V)

**Result: Revenue calculated for all rows**

#### Add Profit % Column (create new column J)
1. Click on the first row of column J (J1)
2. Type header: **Profit %**
3. In J2, enter formula: `=IF(I2=0,0,(H2/I2)*100)`
   - This calculates profit percentage (profit ÷ revenue × 100)
   - IF statement prevents division by zero errors
4. Copy this formula down to all rows
5. Format column J as **Percentage** (0 decimal places)

#### Alternative: Profit % with Better Naming
Create column K with: `=IF(I2=0,0,(H2/I2)*100)` and name it **Profit_Margin_%**

---

## PART 4: EXCEL FORMULAS EXAMPLES

Create a new sheet called **"Formulas Reference"** with these examples:

### Formula 1: VLOOKUP Example
Use case: Look up a product price from a price table

```
=VLOOKUP("Monitor", $A$50:$C$100, 3, FALSE)
```
- Looks up "Monitor" in first column of range A50:C100
- Returns value from 3rd column
- FALSE = exact match

### Formula 2: XLOOKUP (Excel 365+)
More modern alternative to VLOOKUP:

```
=XLOOKUP("Monitor", $A$50:$A$100, $C$50:$C$100, "Not Found")
```
- Looks up value in any column
- Returns value from corresponding cell in return range
- Shows "Not Found" if no match

### Formula 3: IF Condition for High/Low Sales
In a new column (Column K), classify sales as High/Low:

```
=IF(I2>500, "High Sales", "Low Sales")
```

**To classify into 3 tiers:**
```
=IF(I2>=1000, "Premium", IF(I2>=500, "Standard", "Economy"))
```

### Formula 4: SUMIFS for Total Sales by Region
In your Formulas Reference sheet:

**Sum all revenue where region is "North":**
```
=SUMIFS($I$2:$I$35, $D$2:$D$35, "North")
```

**Sum revenue for specific region and category:**
```
=SUMIFS($I$2:$I$35, $D$2:$D$35, "North", $E$2:$E$35, "Electronics")
```

### Formula 5: COUNTIFS Example
Count orders in a specific region:

```
=COUNTIFS($D$2:$D$35, "North", $I$2:$I$35, ">500")
```
Counts rows where Region="North" AND Revenue>500

### Formula 6: SUMPRODUCT for Complex Calculations
Sum revenue with multiple conditions:

```
=SUMPRODUCT(($D$2:$D$35="North")*($E$2:$E$35="Electronics")*($I$2:$I$35))
```

---

## PART 5: PIVOT TABLE ANALYSIS

### Create Pivot Table 1: Sales by Region

1. **Select all data** from "Raw Data" sheet (including headers)
2. Go to **Insert** → **Pivot Table**
3. Choose **New Worksheet** option
4. Click **OK**
5. **Configure the Pivot Table:**
   - **Rows:** Drag "region" to Rows area
   - **Values:** Drag "revenue" to Values area (Sum)
   - **Values:** Drag "profit" to Values area (Sum)

**Result:** Table showing total revenue and profit by region

| Region | Sum of Revenue | Sum of Profit |
|--------|---|---|
| East | $5,250 | $1,095 |
| North | $4,005 | $929 |
| South | $7,185 | $1,635 |
| West | $4,920 | $1,074 |
| **Grand Total** | **$21,360** | **$4,733** |

### Create Pivot Table 2: Sales by Category

1. Follow steps 1-4 from above (create new pivot table)
2. **Configure:**
   - **Rows:** Drag "product_category" to Rows area
   - **Values:** Drag "revenue" to Values area (Sum)
   - **Values:** Drag "quantity" to Values area (Sum)

**Result:** Table showing revenue and quantity by product category

### Create Pivot Table 3: Monthly Sales Trend

1. Create new pivot table from Raw Data
2. **Configure:**
   - **Rows:** Drag "order_date" to Rows area
   - **Values:** Drag "revenue" to Values area (Sum)
3. **Right-click** on dates → **Group** → **By months** (or days/weeks)

**Result:** Monthly breakdown of sales trends

---

## PART 6: DASHBOARD DESIGN

### Step 7: Create Dashboard Sheet

1. **Create a new sheet** and name it **"Dashboard"**
2. Set up the layout with sections for KPIs, charts, and filters

### Step 8: Add KPI Cards

**KPI 1: Total Sales (Cell B2)**

1. In cell B2, add a formula:
   ```
   =SUM(D2:D35) [from Raw Data sheet]
   ```
   Better reference: `=SUM('Raw Data'!I:I)`

2. Format:
   - Font: Bold, Size 28
   - Number Format: Currency ($)
   - Background: Light Blue
   - Borders: Thick border

3. Add label in cell B1: **Total Sales**
   - Font: Size 14, Bold, Gray

**KPI 2: Total Profit (Cell D2)**

1. Formula: `=SUM('Raw Data'!H:H)` [assuming profit is in column H]
2. Format: Bold, Size 28, Currency, Light Green background

**KPI 3: Total Orders (Cell F2)**

1. Formula: `=COUNTA('Raw Data'!A:A)-1` [counts non-empty cells minus header]
2. Format: Bold, Size 28, Light Orange background

**KPI 4: Average Order Value (Cell H2)**

1. Formula: `=AVERAGE('Raw Data'!I:I)`
2. Format: Currency

### Step 9: Add Visualization Charts

#### Chart 1: Sales by Region (Bar Chart)

1. Go to **Formulas Reference** sheet or create summary data
2. Create a small table:
   | Region | Revenue |
   |--------|---------|
   | North  | 4005    |
   | South  | 7185    |
   | East   | 5250    |
   | West   | 4920    |

3. Select this data range
4. Go to **Insert** → **Chart** → **Clustered Bar Chart**
5. Configure chart:
   - Title: "Sales by Region"
   - X-axis: Region
   - Y-axis: Revenue
   - Display data labels
6. Copy and paste into Dashboard sheet
7. Resize to fit below the KPI cards

#### Chart 2: Category Distribution (Pie Chart)

1. Create summary by category using Pivot Table data
2. Select category and revenue data
3. Insert **Pie Chart**
4. Title: "Sales by Product Category"
5. Display percentages and legend
6. Place next to or below the bar chart

#### Chart 3: Monthly Sales Trend (Line Chart)

1. Create monthly summary:
   | Month | Revenue |
   |-------|---------|
   | Jan   | 5500    |
   | Feb   | 8200    |
   | Mar   | 7660    |

2. Select data and insert **Line Chart**
3. Title: "Monthly Sales Trend"
4. Add data labels
5. Add trendline (optional):
   - Right-click line series → **Add Trendline** → **Linear**

### Step 10: Add Slicers for Interactivity

#### Slicer 1: Filter by Region

1. Click on Pivot Table (Pivot Table 1: Sales by Region)
2. Go to **Insert** → **Slicer**
3. Select **"region"** field
4. Click **OK**
5. Drag slicer to dashboard (resize as needed)
6. Style: Choose a professional theme

#### Slicer 2: Filter by Category

1. Click on Pivot Table (Pivot Table 2: Sales by Category)
2. Go to **Insert** → **Slicer**
3. Select **"product_category"**
4. Place on dashboard next to region slicer

### Step 11: Optional - Add Advanced Filters

**Dynamic KPI that changes with slicer selection:**

Instead of static SUM formulas, use SUBTOTAL function with Pivot Tables:

```
=SUBTOTAL(109, 'Raw Data'!I:I)
```
- 109 = SUM (ignores hidden rows)
- Links KPIs to slicer selections when positioned correctly

---

## PART 7: FINAL DASHBOARD LAYOUT

### Recommended Dashboard Structure:

```
┌─────────────────────────────────────────────────────────┐
│           SALES ANALYTICS DASHBOARD                     │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  Total Sales: $21,360  |  Total Profit: $4,733          │
│  Total Orders: 32     |  Avg Order Value: $668          │
│                                                           │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  [Region Slicer]              [Category Slicer]         │
│                                                           │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  Sales by Region (Bar)   |   Sales by Category (Pie)    │
│  ████ North             │   ★ Electronics 35%          │
│  ██████ South           │   ★ Furniture 30%            │
│  █████ East             │   ★ Software 35%             │
│  █████ West             │                               │
│                                                           │
├─────────────────────────────────────────────────────────┤
│                                                           │
│        Monthly Sales Trend (Line Chart)                  │
│        $9,000 ↗                                         │
│        $8,000                                           │
│        $7,000 ─╱─                                       │
│        $6,000 ╱                                         │
│        $5,000 ╱─                                        │
│              Jan    Feb    Mar                           │
│                                                           │
└─────────────────────────────────────────────────────────┘
```

---

## PART 8: STEP-BY-STEP EXCEL WORKFLOW

### Complete Checklist:

- [ ] **Step 1:** Import CSV data
- [ ] **Step 2:** Remove duplicate rows (2 duplicates removed)
- [ ] **Step 3:** Handle missing values (fill with "Unknown" or appropriate values)
- [ ] **Step 4:** Format date column (YYYY-MM-DD or MM/DD/YYYY)
- [ ] **Step 5:** Verify data quality
- [ ] **Step 6:** Add Revenue and Profit % calculated columns
- [ ] **Step 7:** Create formulas reference sheet with VLOOKUP, IF, SUMIFS examples
- [ ] **Step 8:** Create Pivot Table - Sales by Region
- [ ] **Step 9:** Create Pivot Table - Sales by Category
- [ ] **Step 10:** Create Pivot Table - Monthly Sales Trend
- [ ] **Step 11:** Create Dashboard sheet
- [ ] **Step 12:** Add KPI cards (Total Sales, Profit, Orders, Avg Value)
- [ ] **Step 13:** Add Bar chart (Sales by Region)
- [ ] **Step 14:** Add Pie chart (Sales by Category)
- [ ] **Step 15:** Add Line chart (Monthly Trend)
- [ ] **Step 16:** Add Region slicer
- [ ] **Step 17:** Add Category slicer
- [ ] **Step 18:** Test dashboard interactivity
- [ ] **Step 19:** Format dashboard colors and fonts
- [ ] **Step 20:** Add titles and labels

---

## PART 9: ADDITIONAL TIPS & BEST PRACTICES

### Data Quality Checks
- Use **Data Validation** to restrict future entries
- Add **Conditional Formatting** to highlight anomalies (e.g., negative profit, extreme values)
- Create a data entry template with drop-downs for regions and categories

### Performance Optimization
- Use **Table Format** (Ctrl+T) for automatic formula expansion
- Use named ranges for easier formula writing
- Consider Excel Tables instead of ranges for better performance

### Documentation
- Add a "Legend" sheet explaining abbreviations and calculations
- Document formulas used in each column
- Create a "Change Log" to track modifications

### Security
- Protect sensitive sheets with passwords
- Use **Sheet Protection** to prevent accidental edits
- Lock formula cells in calculated columns

---

## Expected Results Summary

**After completing all steps:**

✓ Clean dataset with 32 records (no duplicates)
✓ Properly formatted dates and calculated columns
✓ Revenue and Profit % calculations complete
✓ 3 functional Pivot Tables for different analyses
✓ Professional dashboard with:
  - 4 KPI metrics
  - 3 interactive charts (Bar, Pie, Line)
  - 2 region/category slicers
  - Clean, professional layout
✓ Collection of reusable Excel formulas
✓ Full data analysis capability ready for reports

---

## Files Included

- **sample_sales_data.csv** - Raw data with missing values and duplicates
- **EXCEL_PROJECT_GUIDE.md** - This complete guide (you are here)
- **generate_sample_data.py** - Python script to regenerate data if needed

**Ready to build your Excel dashboard! Follow the steps in sequence for best results.**
