from xmlrpc.client import FastParser

import pandas as pd

# Creating a DataFrame with sample data
data = {
    "product_id": [1, 2, 3, 4, 5, 6],
    "product_name": ["Laptop", "Smartphone", "Tablet", "Smartwatch", "Headphones", "MacBook"],
    "price": [1200, 800, 500, 200, 800, 800],
    "quantity_sold": [30, 50, 20, 15, 45, 10]
}

df = pd.DataFrame(data)
print(df)

sorted_by_price = df.sort_values(by="price")
print(sorted_by_price)

sorted_by_price_and_quantity = df.sort_values(by=["price", "quantity_sold"], ascending=[True, False])
print(sorted_by_price_and_quantity)

df.set_index("product_id", inplace=True)
print(df)

sorted_by_index = df.sort_index()
print(sorted_by_index)
