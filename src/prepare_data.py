from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"


def load_csv_files() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Load raw CSV files used in the project."""
    sales_df = pd.read_csv(RAW_DIR / "sales_data.csv")
    product_df = pd.read_csv(RAW_DIR / "product_master.csv")
    employee_df = pd.read_csv(RAW_DIR / "emp_master.csv")
    return sales_df, product_df, employee_df


def clean_and_prepare_data(
    sales_df: pd.DataFrame, product_df: pd.DataFrame, employee_df: pd.DataFrame
) -> tuple[pd.DataFrame, dict]:
    """Clean source data, enrich it with dimensions, and calculate metrics."""
    total_input_rows = len(sales_df)

    # Rename source columns once so the rest of the pipeline uses consistent names.
    sales_df = sales_df.rename(
        columns={
            "Date": "order_date",
            "EMP ID": "emp_id",
            "Product ID": "product_id",
            "Unit Sold": "unit_sold",
        }
    )
    product_df = product_df.rename(
        columns={
            "Product ID": "product_id",
            "Product Name": "product_name",
            "Price per unit": "price_per_unit",
        }
    )
    employee_df = employee_df.rename(
        columns={
            "EMP ID": "emp_id",
            "EMP Name": "emp_name",
            "Supervisor": "supervisor",
        }
    )

    sales_df["order_date"] = pd.to_datetime(sales_df["order_date"], errors="coerce")
    sales_df["unit_sold"] = pd.to_numeric(sales_df["unit_sold"], errors="coerce")
    product_df["price_per_unit"] = pd.to_numeric(
        product_df["price_per_unit"], errors="coerce"
    )

    # Drop rows that cannot be trusted for downstream analysis.
    required_columns = ["order_date", "emp_id", "product_id", "unit_sold"]
    null_rows_removed = int(sales_df[required_columns].isna().any(axis=1).sum())
    sales_df = sales_df.dropna(subset=required_columns)

    before_dedup = len(sales_df)
    sales_df = sales_df.drop_duplicates()
    duplicate_rows_removed = before_dedup - len(sales_df)

    # Join lookup tables and calculate revenue at the transaction level.
    clean_df = (
        sales_df.merge(product_df, on="product_id", how="left")
        .merge(employee_df, on="emp_id", how="left")
        .assign(
            order_year=lambda df: df["order_date"].dt.year,
            order_month=lambda df: df["order_date"].dt.to_period("M").astype(str),
            total_sales=lambda df: df["unit_sold"] * df["price_per_unit"],
        )
    )

    clean_df = clean_df[
        [
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
    ].sort_values(["order_date", "emp_id", "product_id"])

    metrics = {
        "raw_rows": total_input_rows,
        "clean_rows": len(clean_df),
        "null_rows_removed": null_rows_removed,
        "duplicate_rows_removed": duplicate_rows_removed,
    }
    return clean_df, metrics


def main() -> None:
    """Run the cleaning pipeline and save the processed dataset."""
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    sales_df, product_df, employee_df = load_csv_files()
    clean_df, metrics = clean_and_prepare_data(sales_df, product_df, employee_df)

    clean_df.to_csv(PROCESSED_DIR / "ecommerce_sales_clean.csv", index=False)

    print("Prepared clean dataset successfully.")
    print(metrics)


if __name__ == "__main__":
    main()
