
import pandas as pd

print("Pandas version:", pd.__version__)

df = pd.DataFrame({
    "Product": ["Keyboard", "Mouse", "Monitor"],
    "Sales": [1200, 650, 9500]
})

print("\nSample data:")
print(df)

print("\nTotal sales:", df["Sales"].sum())

