import pandas as pd

# Creating a DataFrame with sample sales data
data = {
    "order_id": [1, 2, 3, 4, 5, 6],
    "product": ["Laptop", "Smartphone", "Laptop", "Tablet", "Smartphone", "Tablet"],
    "region": ["North", "South", "West", "East", "South", "East"],
    "sales": [1200, 800, 1500, 500, 700, 450]
}

df = pd.DataFrame(data)
print(df)

sales_grp = df.groupby("product")["sales"].agg(["sum", "mean", "min", "max", "count"])
print(sales_grp)

sales_region_grp = df.groupby(["product", "region"])["sales"].agg(["sum", "mean", "min", "max", "count"]).reset_index()
print(sales_region_grp)

