import pandas as pd

# Creating a dataset
data = {
    "order_id": [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
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
    ],
    "sales": [1500, 900, 1200, 600, 750, 450, 320, 1400, 200, 380],
}

df = pd.DataFrame(data)
print(df)

#Create a pivot table that shows the total sales (sales) for each product category (category).
#Which category has the highest total sales? Write the answer in a text block.

category_pivot_NaN = pd.pivot_table(df, values="sales",index="category",aggfunc="sum")
print(category_pivot_NaN)

#Highest sales in Electronics category


#Create a pivot table that shows the total sales for each product (product) in each region (region).
# Which product had the highest sales in the North region? Write the answer in a text block.

product_region_pivot=pd.pivot_table(df,values="sales",index="product",columns="region",aggfunc="sum")
print(product_region_pivot)
# Laptop had the highest sales in the North region


#Create a pivot table that shows the total sales and average sales for each product category (category).
# What is the average sales amount for the Electronics category? Write the answer in a text block.

avg_sales_category = pd.pivot_table(df, values="sales",index="category", aggfunc=["sum", "mean"])
print(avg_sales_category)

#Average sales amount for the Electronics category is 971.43


#Create a pivot table using the fill_value=0 parameter that shows the total sales for each product and region.
product_region_pivot = pd.pivot_table(df, values="sales", index="product", columns="region", aggfunc="sum",fill_value=0)
print(product_region_pivot)
