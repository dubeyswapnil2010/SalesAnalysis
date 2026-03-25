-- Total revenue and units sold across the full dataset
SELECT
    SUM(unit_sold) AS total_units_sold,
    SUM(total_sales) AS total_revenue
FROM ecommerce_sales_clean;

-- Monthly sales trend
SELECT
    order_month,
    SUM(unit_sold) AS total_units,
    SUM(total_sales) AS total_sales
FROM ecommerce_sales_clean
GROUP BY order_month
ORDER BY order_month;

-- Top 10 products by revenue
SELECT
    product_id,
    product_name,
    SUM(unit_sold) AS total_units,
    SUM(total_sales) AS total_sales
FROM ecommerce_sales_clean
GROUP BY product_id, product_name
ORDER BY total_sales DESC
LIMIT 10;

-- Employee performance summary
SELECT
    emp_id,
    emp_name,
    supervisor,
    SUM(unit_sold) AS total_units,
    SUM(total_sales) AS total_sales
FROM ecommerce_sales_clean
GROUP BY emp_id, emp_name, supervisor
ORDER BY total_sales DESC;

-- Revenue contribution by supervisor
SELECT
    supervisor,
    SUM(total_sales) AS total_sales
FROM ecommerce_sales_clean
GROUP BY supervisor
ORDER BY total_sales DESC;

-- Average daily revenue
SELECT
    order_date,
    AVG(total_sales) AS average_transaction_value,
    SUM(total_sales) AS daily_revenue
FROM ecommerce_sales_clean
GROUP BY order_date
ORDER BY order_date;
