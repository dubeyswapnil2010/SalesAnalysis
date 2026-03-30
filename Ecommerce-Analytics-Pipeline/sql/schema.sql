CREATE TABLE ecommerce_sales_clean (
    order_date DATE,
    order_year INTEGER,
    order_month VARCHAR(7),
    emp_id VARCHAR(20),
    emp_name VARCHAR(100),
    supervisor VARCHAR(100),
    product_id VARCHAR(20),
    product_name VARCHAR(100),
    unit_sold INTEGER,
    price_per_unit DECIMAL(12, 2),
    total_sales DECIMAL(14, 2)
);
