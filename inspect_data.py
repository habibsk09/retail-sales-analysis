
import pandas as pd
from pathlib import Path

# Locate the dataset relative to this Python file
project_dir = Path(__file__).resolve().parent
file_path = project_dir / "data" / "raw_sales_data.csv"

# Load the raw dataset
df = pd.read_csv(file_path)

# 1. Number of rows and columns
print("1. DATASET SHAPE")
print(df.shape)

# 2. Column names
print("\n2. COLUMN NAMES")
print(df.columns.tolist())

# 3. First five rows
print("\n3. FIRST FIVE ROWS")
print(df.head())

# 4. Data types and non-null counts
print("\n4. DATA TYPES AND NON-NULL COUNTS")
df.info()


# 5. Count missing values in each column
print("\n5. MISSING VALUES")
print(df.isnull().sum())

# 6. Count duplicate rows
print("\n6. DUPLICATE ROWS")
print(df.duplicated().sum())

# 7. Check invalid quantities
print("\n7. INVALID QUANTITIES")
print(df[df["Quantity"] <= 0])

# 8. Check whether Total_Amount is correct
print("\n8. INCORRECT TOTAL AMOUNTS")
expected_total = df["Quantity"] * df["Unit_Price"]
print(df[df["Total_Amount"] != expected_total])

# 9. Check blank text values
print("\n9. BLANK PRODUCT VALUES")
print((df["Product"].fillna("").str.strip() == "").sum())

print("\nBLANK CITY VALUES")
print((df["City"].fillna("").str.strip() == "").sum())
