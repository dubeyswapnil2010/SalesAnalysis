from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_FILE = BASE_DIR / "data" / "processed" / "ecommerce_sales_clean.csv"
REPORTS_DIR = BASE_DIR / "reports"


def load_clean_data() -> pd.DataFrame:
    """Load the processed sales data."""
    df = pd.read_csv(PROCESSED_FILE, parse_dates=["order_date"])
    return df


def build_monthly_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate revenue and units by month."""
    monthly_sales = (
        df.groupby("order_month", as_index=False)
        .agg(total_units=("unit_sold", "sum"), total_sales=("total_sales", "sum"))
        .sort_values("order_month")
    )
    return monthly_sales


def build_top_products(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    """Identify the best-performing products by revenue."""
    top_products = (
        df.groupby(["product_id", "product_name"], as_index=False)
        .agg(total_units=("unit_sold", "sum"), total_sales=("total_sales", "sum"))
        .sort_values("total_sales", ascending=False)
        .head(top_n)
    )
    return top_products


def build_employee_performance(df: pd.DataFrame) -> pd.DataFrame:
    """Summarize performance at the employee level."""
    employee_performance = (
        df.groupby(["emp_id", "emp_name", "supervisor"], as_index=False)
        .agg(
            total_units=("unit_sold", "sum"),
            total_sales=("total_sales", "sum"),
            active_days=("order_date", "nunique"),
        )
        .sort_values("total_sales", ascending=False)
    )
    return employee_performance


def generate_insights(
    df: pd.DataFrame,
    monthly_sales: pd.DataFrame,
    top_products: pd.DataFrame,
    employee_performance: pd.DataFrame,
) -> str:
    """Create a short business insight summary for the dataset."""
    # The source data has employee and supervisor dimensions, but no customer ID.
    # Employee performance is used here as the closest available behavioral view.
    total_units = int(df["unit_sold"].sum())
    total_revenue = float(df["total_sales"].sum())
    top_month = monthly_sales.sort_values("total_sales", ascending=False).iloc[0]
    top_product = top_products.iloc[0]
    top_employee = employee_performance.iloc[0]

    return "\n".join(
        [
            "# E-commerce Sales Insights",
            "",
            f"- Clean transactions: {len(df)}",
            f"- Total units sold: {total_units}",
            f"- Total revenue: {total_revenue:,.2f}",
            f"- Top month by revenue: {top_month['order_month']} ({top_month['total_sales']:,.2f})",
            f"- Best-selling product by revenue: {top_product['product_name']} / {top_product['product_id']} ({top_product['total_sales']:,.2f})",
            f"- Top employee by revenue: {top_employee['emp_name']} / {top_employee['emp_id']} ({top_employee['total_sales']:,.2f})",
        ]
    )


def main() -> None:
    """Generate report files from the cleaned dataset."""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    df = load_clean_data()
    monthly_sales = build_monthly_sales(df)
    top_products = build_top_products(df)
    employee_performance = build_employee_performance(df)
    insight_text = generate_insights(df, monthly_sales, top_products, employee_performance)

    monthly_sales.to_csv(REPORTS_DIR / "monthly_sales_trend.csv", index=False)
    top_products.to_csv(REPORTS_DIR / "top_products.csv", index=False)
    employee_performance.to_csv(REPORTS_DIR / "employee_performance.csv", index=False)
    (REPORTS_DIR / "insights.md").write_text(insight_text, encoding="utf-8")

    print("Analysis reports generated successfully.")


if __name__ == "__main__":
    main()
