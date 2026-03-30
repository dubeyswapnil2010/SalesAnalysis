"""
Excel Data Analyst Project - Sample Data Generator
This script generates realistic sales data with missing values and duplicates
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seeds for reproducibility
np.random.seed(42)
random.seed(42)

# Define data parameters
REGIONS = ['North', 'South', 'East', 'West']
CATEGORIES = ['Electronics', 'Furniture', 'Software']
PRODUCTS = {
    'Electronics': ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Printer'],
    'Furniture': ['Office Chair', 'Desk', 'Bookshelf', 'Table', 'Cabinet'],
    'Software': ['Microsoft Office', 'Adobe Suite', 'Antivirus', 'VPN', 'Project Management']
}
CUSTOMERS = ['John Smith', 'Sarah Johnson', 'Michael Brown', 'Emily Davis', 
             'Robert Wilson', 'Jennifer Taylor', 'David Lee', 'Lisa Martinez']

PRICES = {
    'Laptop': 1200,
    'Monitor': 300,
    'Keyboard': 45,
    'Mouse': 25,
    'Printer': 350,
    'Office Chair': 150,
    'Desk': 400,
    'Bookshelf': 120,
    'Table': 200,
    'Cabinet': 180,
    'Microsoft Office': 200,
    'Adobe Suite': 500,
    'Antivirus': 50,
    'VPN': 100,
    'Project Management': 150
}

PROFIT_MARGIN = {
    'Laptop': 0.30,
    'Monitor': 0.40,
    'Keyboard': 0.80,
    'Mouse': 0.20,
    'Printer': 0.40,
    'Office Chair': 0.50,
    'Desk': 0.30,
    'Bookshelf': 0.25,
    'Table': 0.35,
    'Cabinet': 0.40,
    'Microsoft Office': 0.80,
    'Adobe Suite': 0.80,
    'Antivirus': 0.90,
    'VPN': 0.85,
    'Project Management': 0.85
}

def generate_sample_data(num_records=34, missing_rate=0.15, duplicate_rate=0.08):
    """
    Generate sample sales data with missing values and duplicates
    
    Parameters:
    - num_records: Number of initial records to generate
    - missing_rate: Percentage of data points to set as missing
    - duplicate_rate: Percentage of records to duplicate
    """
    
    data = []
    start_date = datetime(2024, 1, 1)
    
    # Generate initial records
    for i in range(int(num_records * (1 - duplicate_rate))):
        order_id = f"O{str(i+1).zfill(3)}"
        order_date = start_date + timedelta(days=random.randint(0, 90))
        region = random.choice(REGIONS)
        category = random.choice(CATEGORIES)
        product = random.choice(PRODUCTS[category])
        customer = random.choice(CUSTOMERS)
        quantity = random.randint(1, 10)
        price = PRICES[product]
        revenue = quantity * price
        profit = revenue * PROFIT_MARGIN[product]
        
        data.append({
            'order_id': order_id,
            'order_date': order_date,
            'customer_name': customer,
            'region': region,
            'product_category': category,
            'product_name': product,
            'quantity': quantity,
            'price': price,
            'revenue': revenue,
            'profit': profit
        })
    
    # Add duplicates
    if duplicate_rate > 0:
        num_duplicates = int(num_records * duplicate_rate / 2)  # Divide by 2 because each creates 2 copies
        for _ in range(num_duplicates):
            original_record = random.choice(data)
            data.append(original_record.copy())
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Introduce missing values randomly
    missing_indices = np.random.choice(df.index, int(len(df) * missing_rate), replace=False)
    
    for idx in missing_indices:
        column = random.choice(['customer_name', 'product_category', 'product_name', 'revenue', 'profit'])
        df.at[idx, column] = np.nan
    
    # Sort by date
    df = df.sort_values('order_date').reset_index(drop=True)
    
    # Format date as string
    df['order_date'] = df['order_date'].dt.strftime('%Y-%m-%d')
    
    # Fill numeric NaNs with empty strings for CSV export
    df = df.where(pd.notnull(df), '')
    
    return df

def main():
    """Generate and save sample data"""
    
    print("Generating sample sales data...")
    df = generate_sample_data(num_records=34, missing_rate=0.15, duplicate_rate=0.08)
    
    # Save to CSV
    output_file = 'sample_sales_data.csv'
    df.to_csv(output_file, index=False)
    
    print(f"\n✓ Data generated successfully!")
    print(f"  File saved: {output_file}")
    print(f"  Total records: {len(df)}")
    print(f"\nData Summary:")
    print(f"  - Order date range: {df['order_date'].min()} to {df['order_date'].max()}")
    print(f"  - Regions: {', '.join(df['region'].unique())}")
    print(f"  - Categories: {', '.join(df['product_category'].dropna().unique())}")
    print(f"  - Missing values present: Yes")
    print(f"  - Duplicate records: {len(df) - len(df.drop_duplicates(subset=['order_id']))}")
    print(f"\nReady to import into Excel!")
    
    # Display first few rows
    print(f"\nFirst 5 rows preview:")
    print(df.head())
    
    # Display data quality report
    print(f"\n--- Data Quality Report ---")
    print(f"Missing values by column:")
    missing_summary = df.isnull().sum()
    if missing_summary.sum() > 0:
        print(missing_summary[missing_summary > 0])
    else:
        print("No missing values")

if __name__ == "__main__":
    main()
