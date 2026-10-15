
import pandas as pd
from pathlib import Path

# Locate project files
project_dir = Path(__file__).resolve().parent
data_dir = project_dir / "data"

input_file = data_dir / "raw_sales_data.csv"
output_file = data_dir / "cleaned_sales_data.csv"

# Load raw data
df = pd.read_csv(input_file)

print("Original rows:", len(df))

# 1. Remove exact duplicate rows
df = df.drop_duplicates()
print("After removing duplicates:", len(df))

# 2. Convert blank text values into proper missing values
df["Product"] = df["Product"].replace(r"^\s*$", pd.NA, regex=True)
df["City"] = df["City"].replace(r"^\s*$", pd.NA, regex=True)

# 3. Remove rows with missing critical information
# Product is needed for product-level analysis.
df = df.dropna(subset=["Product"])

# City is not required to calculate sales.
# Preserve the row and label its missing city.
df["City"] = df["City"].fillna("Unknown")

# 4. Remove invalid quantities
df = df[df["Quantity"] > 0].copy()

# 5. Correct total amounts using quantity and unit price
df["Total_Amount"] = df["Quantity"] * df["Unit_Price"]

# 6. Convert Date to datetime
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Save cleaned dataset
df.to_csv(output_file, index=False)

print("Final cleaned rows:", len(df))
print("Missing values remaining:")
print(df.isna().sum())
print("Saved to:", output_file)
