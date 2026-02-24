"""
Use the isna() and sum() methods to determine how many missing values there are in each row and column.

Find the percentage of missing values in each row and column. Are there any rows or columns where the proportion of missing values exceeds 50%? If so, remove them from the dataset.

Perform the following steps to handle missing values:

Fill missing values in the customer_name column with the string "Unknown". Save the result in the same column.
Fill missing values in the product_category column with the string "Miscellaneous". Save the result in the same column.
Fill missing values in the quantity and unit_price columns with the mean value of the respective column. Save the result in the same column.
Fill missing values in the order_date column with the last known order date. Save the result in the same column.

"""
import numpy as np
import pandas as pd

# Creating a DataFrame
data = {
    "order_id": [1001, 1002, 1003, 1004, 1005, 1006, 1007],
    "customer_name": ["Alice", "Bob", None, "David", "Eva", "Frank", None],
    "product_category": ["Electronics", "Clothing", "Electronics", "Books", None, "Clothing", "Books"],
    "quantity": [2, 1, None, 1, 3, None, 4],
    "unit_price": [299.99, 49.99, 199.99, None, 15.99, 79.99, 12.99],
    "order_date": ["2024-08-01", "2024-08-02", "2024-08-03", "2024-08-04", "2024-08-05", "2024-08-06", None]
}

df = pd.DataFrame(data)
print(df)

#Find the percentage of missing values in each row and column.
#Are there any rows or columns where the proportion of missing values exceeds 50%? If so, remove them from the dataset.

#print(df.shape[1])

missing_values_column = df.isna().mean() * 100
print(missing_values_column)

missing_values_rows = df.isna().mean(axis=1) * 100
print(missing_values_rows)


#Fill missing values in the customer_name column with the string "Unknown". Save the result in the same column.
df["customer_name"].replace([np.nan], "Unknown", inplace=True)
print(df)

#Fill missing values in the product_category column with the string "Miscellaneous". Save the result in the same column.
df["product_category"].replace([np.nan], "Miscellaneous", inplace=True)
print(df)

#Fill missing values in the quantity and unit_price columns with the mean value of the respective column. Save the result in the same column.
#mn=df["quantity"].mean()

df["quantity"].replace([np.nan], df["quantity"].mean(), inplace=True)
print(df)

df["unit_price"].replace([np.nan], df["unit_price"].mean(), inplace=True)
print(df)

#Fill missing values in the order_date column with the last known order date. Save the result in the same column.

df["order_date"].replace([np.nan], df["order_date"].ffill(), inplace=True)
print(df)

