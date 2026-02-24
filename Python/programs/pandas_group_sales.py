"""
In this task:

Find the total sales for each product category.

Find the average sales for each region. Sort the results in descending order.

Find the average sales for each product across regions.

Find the maximum and minimum sales in each region.
"""
import pandas as pd

# Creating a DataFrame with sample e-commerce data
data = {
    "order_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "product_name": [
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
    ],
    "customer_region": [
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
    ],
    "sales": [1200, 800, 1500, 500, 850, 400, 300, 1300, 150, 350],
}

df = pd.DataFrame(data)
print(df)

#Find the total sales for each product category.

total_sales=df.groupby("category")["sales"].sum()
print(total_sales)


#Find the average sales for each region. Sort the results in descending order.
avg_sales = df.groupby("customer_region")["sales"].mean().reset_index()
print(avg_sales)

avg_sales_sorted=avg_sales.sort_values(by=["sales"], ascending=False)
print(avg_sales_sorted)


#Find the average sales for each product across regions.
avg_sales_region = df.groupby(["product_name","customer_region"])["sales"].mean().reset_index()
print(avg_sales_region)


#Find the maximum and minimum sales in each region.
agg_sales = df.groupby("customer_region")["sales"].agg(["min", "max" ]).reset_index()
print(agg_sales)

