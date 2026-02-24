import pandas as pd
# Creating a DataFrame with sample sales data
data = {
    "order_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111],
    "product": [
        "Laptop",
        "Smartphone",
        "Laptop",
        "Tablet",
        "Smartphone",
        "Tablet",
        "Smartwatch",
        "Laptop",
        "Headphones",
        "Smartwatch",
        "Laptop",
    ],
    "category": [
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Wearables",
        "Electronics",
        "Accessories",
        "Wearables",
        "Electronics",
    ],
    "region": [
        "North",
        "South",
        "East",
        "North",
        "West",
        "South",
        "East",
        "West",
        "North",
        "West",
        "East",
    ],
    "sales": [1200, 800, 1550, 500, 850, 400, 300, 2200, 150, 350, 400],
}

df = pd.DataFrame(data)
print(df)
