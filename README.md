# E-commerce Sales Analysis

This project is an end-to-end analytics workflow built with Python, SQL, and Power BI using an e-commerce sales dataset.

The project covers:

- Loading sales data from CSV files
- Cleaning nulls and duplicates
- Enriching transactions with product and employee master data
- Analyzing sales trends, top products, and employee performance
- Exporting clean data for Power BI dashboards

## Project Structure

```text
.
|-- data
|   |-- raw
|   |   |-- sales_data.csv
|   |   |-- product_master.csv
|   |   `-- emp_master.csv
|   `-- processed
|       `-- ecommerce_sales_clean.csv
|-- dashboard
|   `-- power_bi_notes.md
|-- notebooks
|-- reports
|   |-- employee_performance.csv
|   |-- insights.md
|   |-- monthly_sales_trend.csv
|   `-- top_products.csv
|-- sql
|   |-- analysis_queries.sql
|   `-- schema.sql
|-- src
|   |-- analyze_sales.py
|   |-- export_for_power_bi.py
|   `-- prepare_data.py
`-- requirements.txt
```

## Dataset

The source workbook provided was:

- `c:\Users\dubey\OneDrive\Desktop\ecommerce-sales-analysis\Data\Sales Data.xlsx`

For this project, the workbook was converted into CSV inputs so the analytics flow starts from CSV files as requested:

- `data/raw/sales_data.csv`
- `data/raw/product_master.csv`
- `data/raw/emp_master.csv`

## Data Model

The cleaned dataset joins the transaction table with lookup tables and produces these core fields:

- `order_date`
- `order_year`
- `order_month`
- `emp_id`
- `emp_name`
- `supervisor`
- `product_id`
- `product_name`
- `unit_sold`
- `price_per_unit`
- `total_sales`

Note:

- The source workbook does not include customer identifiers or customer profiles.
- To stay close to the requested "customer insights" requirement, this project includes employee and supervisor performance insights as the nearest available business-entity view in the dataset.

## Key Cleaning Steps

The pipeline performs the following cleaning logic:

1. Standardizes column names.
2. Parses dates into proper datetime values.
3. Converts quantity and price columns to numeric types.
4. Removes rows with nulls in required fields.
5. Removes duplicate transactions.
6. Joins product and employee master data.
7. Calculates `total_sales = unit_sold * price_per_unit`.

## Generated Outputs

The repository already includes generated outputs:

- Clean transaction dataset: [data/processed/ecommerce_sales_clean.csv](/c:/Users/dubey/OneDrive/Documents/New%20project/data/processed/ecommerce_sales_clean.csv)
- Monthly sales trend: [reports/monthly_sales_trend.csv](/c:/Users/dubey/OneDrive/Documents/New%20project/reports/monthly_sales_trend.csv)
- Top products summary: [reports/top_products.csv](/c:/Users/dubey/OneDrive/Documents/New%20project/reports/top_products.csv)
- Employee performance summary: [reports/employee_performance.csv](/c:/Users/dubey/OneDrive/Documents/New%20project/reports/employee_performance.csv)
- Insight summary: [reports/insights.md](/c:/Users/dubey/OneDrive/Documents/New%20project/reports/insights.md)

## Current Insights

Based on the generated outputs:

- Raw sales transactions: `6490`
- Clean transactions: `6489`
- Duplicate rows removed: `1`
- Null-key rows removed: `0`
- Total units sold: `1,122,741`
- Total revenue: `96,617,021`
- Best month by revenue: `2019-01`
- Best-selling product by revenue: `Product-7 (P10007)`
- Top employee by revenue: `EMP-4 (10004)`

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run The Pipeline

Prepare the cleaned dataset:

```bash
python src/prepare_data.py
```

Generate reports and insights:

```bash
python src/analyze_sales.py
```

Export the Power BI-ready dataset:

```bash
python src/export_for_power_bi.py
```

## Power BI Usage

1. Open Power BI Desktop.
2. Select `Get Data` -> `Text/CSV`.
3. Load `data/processed/ecommerce_sales_clean.csv`.
4. Use `order_date`, `order_month`, `product_name`, `emp_name`, `supervisor`, `unit_sold`, and `total_sales` for visuals.

Suggested visuals:

- Monthly revenue trend line chart
- Top 10 products by revenue bar chart
- Employee revenue leaderboard
- Product-level sales table
- Supervisor performance comparison

See [dashboard/power_bi_notes.md](/c:/Users/dubey/OneDrive/Documents/New%20project/dashboard/power_bi_notes.md) for dashboard ideas.

## SQL

Sample schema and analysis queries are included here:

- [sql/schema.sql](/c:/Users/dubey/OneDrive/Documents/New%20project/sql/schema.sql)
- [sql/analysis_queries.sql](/c:/Users/dubey/OneDrive/Documents/New%20project/sql/analysis_queries.sql)

## Notes

- The Python scripts are written to use CSV inputs in `data/raw`.
- The workspace currently contains generated CSV outputs, so you can open them directly in Power BI without waiting for additional processing.
