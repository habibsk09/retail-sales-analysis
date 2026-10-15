
import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

# Reproducible random data
random.seed(42)

# Product catalog
products = [
    ("Keyboard", "Electronics", 1200),
    ("Mouse", "Electronics", 650),
    ("Monitor", "Electronics", 9500),
    ("Notebook", "Stationery", 80),
    ("Pen", "Stationery", 20),
    ("Backpack", "Accessories", 1500),
    ("Water Bottle", "Accessories", 350),
    ("Headphones", "Electronics", 2200),
]

cities = ["Kolkata", "Delhi", "Mumbai", "Bangalore"]
payment_methods = ["UPI", "Cash", "Card"]

rows = []

# Generate 200 sales records
for i in range(1, 201):
    product, category, price = random.choice(products)
    quantity = random.randint(1, 5)

    date = datetime(2026, 1, 1) + timedelta(
        days=random.randint(0, 89)
    )

    rows.append({
        "Order_ID": f"ORD{i:04d}",
        "Date": date.strftime("%Y-%m-%d"),
        "Product": product,
        "Category": category,
        "Quantity": quantity,
        "Unit_Price": price,
        "Total_Amount": quantity * price,
        "City": random.choice(cities),
        "Payment_Method": random.choice(payment_methods),
    })

# Add intentional data quality issues

# Duplicate records
rows.extend([rows[4].copy(), rows[14].copy()])

# Missing value
rows[10]["City"] = ""

# Invalid quantity
rows[20]["Quantity"] = -2

# Incorrect total
rows[30]["Total_Amount"] = 99999

# Missing product
rows[40]["Product"] = ""

# Save CSV inside the data folder
project_dir = Path(__file__).resolve().parent
output_dir = project_dir / "data"
output_dir.mkdir(exist_ok=True)

output_file = output_dir / "raw_sales_data.csv"

with output_file.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print("Dataset created successfully!")
print(f"Total records: {len(rows)}")
print(f"Saved to: {output_file}")
