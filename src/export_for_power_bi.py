from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_FILE = BASE_DIR / "data" / "processed" / "ecommerce_sales_clean.csv"
REPORTS_DIR = BASE_DIR / "reports"


def export_power_bi_ready_files() -> None:
    """Save CSV files that are convenient to import directly into Power BI."""
    df = pd.read_csv(PROCESSED_FILE, parse_dates=["order_date"])

    # Keep a stable column order so Power BI imports are predictable.
    export_columns = [
        "order_date",
        "order_year",
        "order_month",
        "emp_id",
        "emp_name",
        "supervisor",
        "product_id",
        "product_name",
        "unit_sold",
        "price_per_unit",
        "total_sales",
    ]

    power_bi_export = df[export_columns].sort_values(["order_date", "product_id", "emp_id"])
    power_bi_export.to_csv(PROCESSED_FILE, index=False)

    # These helper tables are useful if you want separate visuals or supporting tables.
    (
        df.groupby("order_month", as_index=False)
        .agg(total_units=("unit_sold", "sum"), total_sales=("total_sales", "sum"))
        .to_csv(REPORTS_DIR / "monthly_sales_trend.csv", index=False)
    )

    (
        df.groupby(["product_id", "product_name"], as_index=False)
        .agg(total_units=("unit_sold", "sum"), total_sales=("total_sales", "sum"))
        .sort_values("total_sales", ascending=False)
        .head(10)
        .to_csv(REPORTS_DIR / "top_products.csv", index=False)
    )


if __name__ == "__main__":
    export_power_bi_ready_files()
    print("Power BI export completed.")
