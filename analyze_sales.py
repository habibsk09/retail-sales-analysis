
import pandas as pd
from pathlib import Path

# Locate the cleaned dataset
project_dir = Path(__file__).resolve().parent
file_path = project_dir / "data" / "cleaned_sales_data.csv"

df = pd.read_csv(file_path, parse_dates=["Date"])

# 1. Overall business summary
total_revenue = df["Total_Amount"].sum()
total_orders = df["Order_ID"].nunique()
total_units = df["Quantity"].sum()
average_order_value = total_revenue / total_orders

print("=" * 40)
print("OVERALL SALES SUMMARY")
print("=" * 40)

print(f"Total Revenue: Rs. {total_revenue:,.2f}")
print(f"Unique Orders: {total_orders}")
print(f"Units Sold: {total_units}")
print(f"Average Order Value: Rs. {average_order_value:,.2f}")

# 2. Revenue by product
print("\nREVENUE BY PRODUCT")

product_sales = (
    df.groupby("Product")["Total_Amount"]
    .sum()
    .sort_values(ascending=False)
)

print(product_sales.to_string())

# 3. Revenue by city
print("\nREVENUE BY CITY")

city_sales = (
    df.groupby("City")["Total_Amount"]
    .sum()
    .sort_values(ascending=False)
)

print(city_sales.to_string())

# 4. Monthly revenue
print("\nMONTHLY REVENUE")

monthly_sales = (
    df.groupby(df["Date"].dt.to_period("M"))["Total_Amount"]
    .sum()
    .sort_index()
)

print(monthly_sales.to_string())


import matplotlib.pyplot as plt

# Revenue by product chart
plt.figure(figsize=(10, 6))

product_sales.sort_values().plot(
    kind="barh",
    color="steelblue"
)

plt.title("Revenue by Product")
plt.xlabel("Revenue (INR)")
plt.ylabel("Product")
plt.tight_layout()

# Save the chart
report_dir = project_dir / "reports"
report_dir.mkdir(exist_ok=True)

chart_path = report_dir / "revenue_by_product.png"
plt.savefig(chart_path, dpi=150, bbox_inches="tight")
plt.close()

print(f"\nChart saved to: {chart_path}")
