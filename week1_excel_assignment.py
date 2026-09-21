import pandas as pd

INPUT_FILE = "global_superstore_2016.xlsx"

orders = pd.read_excel(INPUT_FILE, sheet_name="Orders")

# 1. Remove/check duplicates and handle missing values
print("Duplicate rows:", orders.duplicated().sum())
print("Missing values:")
print(orders.isna().sum()[orders.isna().sum() > 0])

cleaned = orders.copy()
cleaned["Postal Code"] = cleaned["Postal Code"].fillna("Not Available")

# 2. Region-wise sales
region_sales = cleaned.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print("\nRegion-wise Sales:\n", region_sales)

# 3. Mean, median, mode
print("\nMean:", orders["Sales"].mean())
print("Median:", orders["Sales"].median())
print("Mode:", orders["Sales"].mode().iloc[0])

# 4. Top 10 sales
top10 = orders.nlargest(10, "Sales")
print("\nTop 10 Sales:\n", top10[["Order ID", "Product Name", "Sales"]])

# 5. Category-wise revenue
category_revenue = cleaned.groupby("Category")["Sales"].sum().sort_values(ascending=False)
print("\nCategory-wise Revenue:\n", category_revenue)
