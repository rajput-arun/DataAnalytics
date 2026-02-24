import pandas as pd

# Creating the first DataFrame with customer data
customers = {
    "customer_id": [1, 2, 3, 4],
    "name": ["Alice", "Bob", "Charlie", "David"],
    "email": [
        "alice@example.com",
        "bob@example.com",
        "charlie@example.com",
        "david@example.com",
    ],
}

df_customers = pd.DataFrame(customers)
print(df_customers)
print()

# Creating the second DataFrame with order data
orders = {
    "order_id": [101, 102, 103, 104],
    "customer_id": [1, 2, 2, 5],
    "product": ["Laptop", "Tablet", "Smartphone", "Laptop"],
    "amount": [1200, 300, 800, 1300],
}

df_orders = pd.DataFrame(orders)
print(df_orders)

# Performing an inner join on "customer_id"
inner_join = pd.merge(df_customers, df_orders, on="customer_id", how="inner")
print(inner_join)


left_join = pd.merge(df_customers, df_orders, on="customer_id", how="left")
print(left_join)

right_join = pd.merge(df_customers, df_orders, on="customer_id", how="right")
print(right_join)

print()

outer_join = pd.merge(df_customers, df_orders, on="customer_id", how="outer")
print(outer_join)

