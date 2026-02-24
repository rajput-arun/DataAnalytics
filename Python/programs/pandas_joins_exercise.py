import pandas as pd

# Creating a DataFrame with product data
products = {
    "product_id": [1, 2, 3, 4],
    "product_name": ["Laptop", "Tablet", "Smartphone", "Smartwatch"],
    "category": ["Electronics", "Electronics", "Electronics", "Wearables"],
    "price": [1200, 300, 800, 250],
}

df_products = pd.DataFrame(products)
print(df_products)

# Creating a DataFrame with order details
order_details = {
    "order_id": [101, 102, 103, 104, 105, 106, 107],
    "product_id": [2, 2, 1, 2, 4, 1, 5],
    "customer_id": [201, 202, 202, 204, 203, 201, 202],
    "quantity": [1, 2, 1, 3, 2, 2, 4],
}

df_order_details = pd.DataFrame(order_details)
print(df_order_details)

#Perform an INNER JOIN between the orders table and the products table based on product_id.
in_join = pd.merge(df_products, df_order_details, on="product_id", how="inner")
print(in_join)

#Perform a LEFT JOIN between the orders table and the products table.
lt_join=pd.merge(df_products, df_order_details, on="product_id", how="left")
print(lt_join)


#Perform an OUTER JOIN between the orders table and the products table.
out_join = pd.merge(df_products, df_order_details, on="product_id", how="outer")
print(out_join)


#Analysis
### Which products were ordered? Laptop, Tablet and Smartwatch
### Which products were not ordered? Smartphone
### Which product ID is missing in the product table? Product ID 5 is not available in product table