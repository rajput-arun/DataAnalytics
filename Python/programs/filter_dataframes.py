import pandas as pd

# Creating a DataFrame with sample data
data = {
    "order_id": [101, 102, 103, 104, 105],
    "product": ["Laptop", "Smartphone", "Tablet", "Smartwatch", "Headphones"],
    "price": [1200, 800, 500, 200, 100],
    "quantity": [3, 5, 2, 8, 10]
}

df = pd.DataFrame(data)
print(df)

high_price = df[
    (df["price"] > 500)  &
    (df["quantity"] > 4)
]
print(high_price)

# Filtering rows with specific product names
specific_products = df[
    df["product"].isin
    (
        ["Laptop", "Smartphone"]
    )
]
print(specific_products)

smart_products = df[
    df["product"].str.contains("Smart")
]
# Filtering rows based on text data
#smart_products = df[df["product"].str.contains("Smart")]
print(smart_products)
