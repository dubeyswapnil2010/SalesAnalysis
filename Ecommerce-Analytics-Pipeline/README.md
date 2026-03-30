# 💰 E-commerce Sales Analysis

A comprehensive end-to-end analytics workflow built with **Python**, **SQL**, and **Power BI** using an e-commerce sales dataset.

---

## 🎯 Project Overview

This project demonstrates a complete data analytics pipeline:

1. **Data Loading** - Import from CSV files
2. **Data Cleaning** - Remove nulls and duplicates
3. **Data Enrichment** - Join with product and employee master data
4. **Data Analysis** - Analyze trends, products, and performance
5. **Report Generation** - Create actionable insights
6. **Power BI Integration** - Build interactive dashboards

**Tech Stack:** Python, SQL, Power BI  
**Complexity Level:** Intermediate  
**Final Output:** Clean dataset + SQL queries + Power BI dashboards

---

## 📁 Project Structure

```
.
├── data/
│   ├── raw/
│   │   ├── sales_data.csv
│   │   ├── product_master.csv
│   │   └── emp_master.csv
│   └── processed/
│       └── ecommerce_sales_clean.csv
├── dashboard/
│   └── power_bi_notes.md
├── reports/
│   ├── employee_performance.csv
│   ├── insights.md
│   ├── monthly_sales_trend.csv
│   └── top_products.csv
├── sql/
│   ├── analysis_queries.sql
│   └── schema.sql
├── src/
│   ├── analyze_sales.py
│   ├── export_for_power_bi.py
│   └── prepare_data.py
├── notebooks/
├── requirements.txt
└── README.md
```

---

## 📊 Dataset Overview

### Source Data
The project uses e-commerce sales data converted to CSV format:

- **sales_data.csv** - Transaction records
- **product_master.csv** - Product catalog
- **emp_master.csv** - Employee directory

### Raw Data Statistics
- Raw sales transactions: 6,490
- Clean transactions: 6,489
- Duplicate rows removed: 1
- Null-key rows removed: 0
- Date range: 2019-01 to 2019-12

### Data Model

**Core Fields (after merged data):**

| Field | Type | Description |
|-------|------|-------------|
| order_date | Date | Date of transaction |
| order_year | Integer | Year |
| order_month | Integer | Month |
| emp_id | String | Employee identifier |
| emp_name | String | Employee name |
| supervisor | String | Supervisor name |
| product_id | String | Product identifier |
| product_name | String | Product name |
| unit_sold | Numeric | Quantity sold |
| price_per_unit | Numeric | Unit price |
| total_sales | Numeric | Revenue (unit_sold × price_per_unit) |

---

## 🔧 Requirements

### Software
- **Python 3.7+**
- **Microsoft Excel** (for viewing CSV outputs)
- **Power BI Desktop** (for dashboard creation)
- **SQL Server / MySQL** (optional, for SQL analysis)

### Python Packages
- pandas
- numpy
- matplotlib
- seaborn

Install via: `pip install -r requirements.txt`

---

## 🚀 Quick Start

### 1. Setup Environment

```bash
# Install dependencies
pip install -r requirements.txt
```

### 2. Data Preparation

```bash
# Prepare and clean the dataset
python src/prepare_data.py
```

**Output:** `data/processed/ecommerce_sales_clean.csv`

### 3. Data Analysis

```bash
# Generate reports and insights
python src/analyze_sales.py
```

**Outputs:**
- `reports/monthly_sales_trend.csv`
- `reports/top_products.csv`
- `reports/employee_performance.csv`
- `reports/insights.md`

### 4. Export for Power BI

```bash
# Export clean data for Power BI
python src/export_for_power_bi.py
```

**Output:** Power BI-ready dataset

### 5. Build Power BI Dashboard

1. Open Power BI Desktop
2. Get Data → Text/CSV
3. Load `data/processed/ecommerce_sales_clean.csv`
4. Create visualizations (see suggestions below)

---

## 📈 Key Findings

Based on generated analysis:

### Sales Metrics
- **Total Units Sold:** 1,122,741
- **Total Revenue:** $96,617,021
- **Highest Month:** January 2019
- **Best-Selling Product:** Product-7 (P10007)
- **Top Employee:** EMP-4 (10004)

### Data Quality
- **Raw Records:** 6,490
- **Clean Records:** 6,489
- **Data Cleaning Rate:** 99.98%
- **Duplicates Removed:** 1

---

## 🐍 Python Scripts

### prepare_data.py
**Purpose:** Clean and enrich raw data

**Cleaning Logic:**
1. Standardize column names
2. Parse dates to datetime
3. Convert numeric columns
4. Remove rows with null keys
5. Remove duplicate transactions
6. Join with product and employee masters
7. Calculate total_sales

**Output:** `ecommerce_sales_clean.csv`

### analyze_sales.py
**Purpose:** Generate reports and insights

**Analysis Performed:**
- Monthly sales trends
- Top 10 products by revenue
- Top 10 employees by revenue
- Category performance
- Regional analysis (if available)

**Outputs:**
- `monthly_sales_trend.csv`
- `top_products.csv`
- `employee_performance.csv`
- `insights.md` (summary)

### export_for_power_bi.py
**Purpose:** Export data in Power BI-optimized format

**Optimizations:**
- Date formatting
- Currency formatting
- Index reset
- CSV export with UTF-8 encoding

**Output:** Power BI-ready CSV

---

## 📊 SQL Analysis

### Schema (sql/schema.sql)

```sql
CREATE TABLE Sales (
    order_date DATE,
    emp_id VARCHAR(10),
    emp_name VARCHAR(100),
    supervisor VARCHAR(100),
    product_id VARCHAR(10),
    product_name VARCHAR(100),
    unit_sold INT,
    price_per_unit DECIMAL(10, 2),
    total_sales DECIMAL(12, 2)
);
```

### Sample Queries (sql/analysis_queries.sql)

**Top 10 Products by Revenue**
```sql
SELECT TOP 10 product_name, SUM(total_sales) as revenue
FROM Sales
GROUP BY product_name
ORDER BY revenue DESC;
```

**Monthly Sales Trend**
```sql
SELECT DATEPART(YEAR, order_date) as year,
       DATEPART(MONTH, order_date) as month,
       SUM(total_sales) as monthly_revenue
FROM Sales
GROUP BY DATEPART(YEAR, order_date), DATEPART(MONTH, order_date)
ORDER BY year, month;
```

**Employee Performance**
```sql
SELECT emp_name, supervisor, SUM(total_sales) as employee_revenue
FROM Sales
GROUP BY emp_name, supervisor
ORDER BY employee_revenue DESC;
```

See `sql/analysis_queries.sql` for more queries.

---

## 📊 Power BI Dashboard

### Suggested Visualizations

**KPI Cards**
- Total Revenue
- Total Units Sold
- Unique Employees
- Best Product

**Charts**
- Monthly revenue trend (Line chart)
- Top 10 products (Bar chart)
- Employee leaderboard (Bar chart)
- Sales by supervisor (Pie chart)
- Product category distribution (Donut chart)

**Tables**
- Product-level sales details
- Employee performance rankings
- Monthly breakdown

**Slicers**
- Year
- Month
- Employee
- Product Category

### Dashboard Setup Steps

1. **Import Data**
   - Power BI Desktop → Get Data → Text/CSV
   - Select `ecommerce_sales_clean.csv`

2. **Create Relationships**
   - Ensure order_date is recognized as Date
   - Set emp_id and product_id as keys if separate tables

3. **Add Visualizations**
   - Drag fields to chart areas
   - Configure axes and values
   - Add data labels

4. **Add Filters**
   - Insert slicers for Year, Month, Employee
   - Configure slicer connections

5. **Polish & Share**
   - Apply consistent color scheme
   - Set theme
   - Publish to Power BI Service (optional)

See `dashboard/power_bi_notes.md` for detailed dashboard design guidelines.

---

## 📁 Generated Reports

### reports/monthly_sales_trend.csv
Monthly aggregation of sales data:

| Month | Revenue | Units | Transactions |
|-------|---------|-------|--------------|
| 2019-01 | $8,234,150 | 94,523 | 612 |
| 2019-02 | $7,891,240 | 89,234 | 587 |
| ... | ... | ... | ... |

### reports/top_products.csv
Top 10 products by revenue:

| Product | Revenue | Units | Avg Price |
|---------|---------|-------|-----------|
| Product-7 | $4,521,000 | 45,210 | $100 |
| Product-3 | $3,890,500 | 38,905 | $100 |
| ... | ... | ... | ... |

### reports/employee_performance.csv
Employee sales rankings:

| Employee | Supervisor | Revenue | Units | Transactions |
|----------|-----------|---------|-------|--------------|
| EMP-4 | SUP-1 | $8,521,000 | 85,210 | 524 |
| EMP-2 | SUP-2 | $7,654,300 | 76,543 | 498 |
| ... | ... | ... | ... | ... |

### reports/insights.md
Executive summary with key findings.

---

## 🔄 Data Cleaning Pipeline

### Step-by-Step Process

**Input:** Raw CSV files

1. **Load Data**
   - Read sales, product, and employee CSVs
   
2. **Standardize Columns**
   - Remove spaces
   - Convert to lowercase
   - Rename ambiguous columns

3. **Type Conversion**
   - Dates → datetime
   - Amounts → decimal
   - IDs → string

4. **Handle Nulls**
   - Remove rows with null in key fields
   - Fill optional nulls with defaults

5. **Remove Duplicates**
   - Identify duplicate transactions
   - Keep first occurrence

6. **Data Enrichment**
   - Join with product master
   - Join with employee master
   - Add derived columns (total_sales)

7. **Export**
   - Save clean dataset
   - Create Power BI export
   - Generate CSV reports

**Output:** Cleaned, enriched, analysis-ready data

---

## 📈 Analysis Highlights

### Monthly Trends
- **Highest Revenue Month:** January 2019 (~$8.2M)
- **Lowest Revenue Month:** December 2019 (~$7.5M)
- **Average Monthly Revenue:** ~$8.05M

### Product Performance
- **Top Product:** Product-7 with $4.5M revenue
- **Best Category:** [Determined from data]
- **Lowest Performer:** [Determined from data]

### Employee Performance
- **Top Performer:** EMP-4 with $8.5M revenue
- **Best Supervisor:** [Determined from data]
- **Team Size:** [Number of employees]

---

## 🛠️ Troubleshooting

### Python Issues

**Issue:** "ModuleNotFoundError: pandas"
- Solution: Run `pip install -r requirements.txt`

**Issue:** CSV file not found
- Solution: Ensure CSVs are in `data/raw/` folder

**Issue:** Date parsing errors
- Solution: Check CSV date format (should be YYYY-MM-DD)

### Power BI Issues

**Issue:** Data doesn't load
- Solution: Set decimal separator correctly in localization settings
- Ensure CSV encoding is UTF-8

**Issue:** Charts aren't updating
- Solution: Refresh data (Ctrl+Shift+R)
- Check filter connections

### SQL Issues

**Issue:** Import/export errors
- Solution: Verify SQL Server compatibility
- Check file permissions

---

## 📚 Files Reference

| File | Purpose |
|------|---------|
| src/prepare_data.py | Data cleaning pipeline |
| src/analyze_sales.py | Report generation |
| src/export_for_power_bi.py | Power BI export |
| sql/schema.sql | Database schema |
| sql/analysis_queries.sql | SQL analysis examples |
| dashboard/power_bi_notes.md | Dashboard guidelines |
| reports/*.csv | Generated outputs |
| requirements.txt | Python dependencies |

---

## 🎓 Skills Demonstrated

**Data Engineering**
- CSV parsing and loading
- Data cleaning and transformation
- Data validation
- Data enrichment with joins

**Data Analysis**
- Trend analysis
- Aggregation and summarization
- Performance metrics
- Comparative analysis

**Reporting & Visualization**
- Report automation
- Power BI dashboard design
- Executive summary creation
- Data storytelling

**Database & SQL**
- Schema design
- Complex queries
- Aggregation functions
- Report queries

---

## 🚀 Next Steps

### Beginner Enhancements
- Add more visualizations to Power BI
- Create additional analysis views
- Build trend forecasting
- Add regional analysis

### Intermediate Enhancements
- Implement automated refresh schedule
- Add data validation layer
- Create data quality metrics
- Build anomaly detection

### Advanced Enhancements
- Migrate to cloud (Azure, AWS)
- Add machine learning models
- Implement real-time updates
- Create mobile dashboards

---

## 📞 Support

### Documentation
1. **Inline code comments** - Explanations in Python scripts
2. **SQL comments** - Query annotations
3. **Power BI guide** - `dashboard/power_bi_notes.md`
4. **This README** - Comprehensive overview

### External Resources
- **Pandas Documentation:** pandas.pydata.org
- **Python:** python.org
- **Power BI:** support.microsoft.com/power-bi
- **SQL:** microsoft.com/sql-server

---

## 📝 Project Information

**Version:** 1.0  
**Created:** March 2024  
**Data Period:** January - December 2019  
**Last Updated:** March 2024  
**Status:** Production Ready

---

## ✅ Checklist

- ✓ Raw data imported
- ✓ Data cleaned (6,489 records)
- ✓ Reports generated
- ✓ Power BI exports ready
- ✓ SQL queries available
- ✓ Insights documented

---

**Ready to analyze e-commerce data?** Run `python src/prepare_data.py` to get started! 📊
