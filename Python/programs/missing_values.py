import numpy as np
import pandas as pd

messy_data = pd.Series([1, np.nan, 2, 4, None]) # there are two types of missing values
print(messy_data)

print(f"Sum of a series with missing values: {messy_data.sum()}")
print(f"Average value of a series with missing values: {messy_data.mean()}")
print(f"Median value of a series with missing values: {messy_data.median()}")

print(messy_data.isna().sum())
print(messy_data.notna().sum())

data = {
    "order_id": [1001, 1002, 1003, 1004, 1005],
    "customer_id": [101, 102, np.nan, 102, 103],
    "product_id": [2001, 2002, 2001, np.nan, 2001],
    "quantity": [1, 2, np.nan, 1, 3],
    "price": [25.5, np.nan, 15.0, 22.0, np.nan],
    "discount": [0.1, 0.2, np.nan, np.nan, 0.05],
    "order_date": ["2024-08-01", "2024-08-02", np.nan, "2024-08-04", "2024-08-05"]
}

sales_df = pd.DataFrame(data)
sales_df.head()

print(sales_df)
print(sales_df["price"].isna().sum())
print(sales_df["price"].notna().sum())
print(sales_df.loc[2,:].isna().sum())
print(sales_df.loc[2,:].notna().sum())
print(sales_df.loc[].notna())
print(sales_df.isna().sum())
print(sales_df.isna().sum(axis=1))
print(sales_df.notna().sum(axis=1))
print(sales_df.shape[1])
print(f"{((sales_df.isna().sum(axis=1) / sales_df.shape[1]) * 100)}%")
print(f"{((sales_df.isna().sum(axis=0) / sales_df.shape[0]) * 100)}%")


print("-"*40)
print(sales_df)

# fill gaps in the "price" column with -999
sales_df["price"].fillna(-999)
print(sales_df)

# delete rows that contain at least one missing value
#sales_af = sales_df.dropna(thresh=5)
# delete rows that contain gaps in specific columns
#sales_af = sales_df.dropna(subset=["customer_id", "product_id"])

#print(sales_af)

