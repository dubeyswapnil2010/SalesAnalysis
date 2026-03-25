# Power BI Dashboard Notes

Use `data/processed/ecommerce_sales_clean.csv` as the main table in Power BI.

Recommended visuals:

- Line chart: `order_month` vs `SUM(total_sales)`
- Clustered bar chart: `product_name` vs `SUM(total_sales)` for top products
- Table: `emp_name`, `supervisor`, `SUM(unit_sold)`, `SUM(total_sales)`
- Card visuals: total revenue, total units sold, total transactions
- Slicers: `order_month`, `supervisor`, `product_name`

Suggested DAX measures:

```DAX
Total Revenue = SUM(ecommerce_sales_clean[total_sales])
Total Units = SUM(ecommerce_sales_clean[unit_sold])
Average Order Value = AVERAGE(ecommerce_sales_clean[total_sales])
```
