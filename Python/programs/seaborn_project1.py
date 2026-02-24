"""
1.  Create a bar chart showing the average revenue for each product category:
    - Arrange the categories in descending order of average revenue.
    - Which category has the highest average sales?
    - Which category sells the least?
    Add traffic source as a color (hue) to the previous chart. Draw conclusions about the popularity of traffic sources.

2.  Build a scatter plot to visualize the relationship between the number of items in an order and the revenue:
    Set the marker size to 100 units for better clarity by adding the parameter s=100.
    What can be said about the nature of the relationship between the number of items in an order and the revenue?
    Add the product category as a color on the scatter plot:
    Choose the "deep" palette for this.
    Are there differences between categories on this chart? How would you describe them?

"""
import seaborn as sns
import matplotlib.pyplot as plt
#import numpy as np
import pandas as pd



# Creating a sample dataset
data = {
    "date": [
        "2024-09-01",
        "2024-09-01",
        "2024-09-02",
        "2024-09-02",
        "2024-09-03",
        "2024-09-03",
        "2024-09-04",
        "2024-09-04",
        "2024-09-05",
        "2024-09-05",
        "2024-09-06",
        "2024-09-06",
        "2024-09-07",
        "2024-09-07",
        "2024-09-08",
        "2024-09-08",
        "2024-09-09",
        "2024-09-09",
        "2024-09-10",
        "2024-09-10",
    ],
    "category": [
        "Electronics",
        "Clothing",
        "Books",
        "Electronics",
        "Furniture",
        "Clothing",
        "Books",
        "Electronics",
        "Furniture",
        "Clothing",
        "Books",
        "Electronics",
        "Furniture",
        "Clothing",
        "Books",
        "Electronics",
        "Furniture",
        "Clothing",
        "Books",
        "Electronics",
    ],
    "units_sold": [
        15,
        30,
        20,
        10,
        5,
        25,
        18,
        8,
        12,
        22,
        25,
        7,
        6,
        28,
        15,
        11,
        7,
        18,
        20,
        12,
    ],
    "revenue_usd": [
        1500,
        750,
        300,
        1200,
        500,
        625,
        270,
        960,
        1200,
        550,
        375,
        840,
        600,
        700,
        225,
        1320,
        700,
        450,
        300,
        1440,
    ],
    "traffic_source": [
        "Direct",
        "Organic Search",
        "Social Media",
        "Direct",
        "Google Ads",
        "Direct",
        "Organic Search",
        "Social Media",
        "Google Ads",
        "Social Media",
        "Organic Search",
        "Direct",
        "Google Ads",
        "Social Media",
        "Organic Search",
        "Direct",
        "Google Ads",
        "Social Media",
        "Direct",
        "Organic Search",
    ],
}

# Створення DataFrame
df = pd.DataFrame(data)
print(df)
avg_df = (
    df.groupby("category",as_index=False)["revenue_usd"]
    .mean()
    .sort_values("revenue_usd", ascending=False)
)
print(avg_df)

"""
1.  Create a bar chart showing the average revenue for each product category:
    - Arrange the categories in descending order of average revenue.
    - Which category has the highest average sales?
    - Which category sells the least?
    Add traffic source as a color (hue) to the previous chart. Draw conclusions about the popularity of traffic sources.

"""

avg_revenue = df.groupby("category")["revenue_usd"].mean()
print(avg_revenue)

#sns.barplot(x="category", y=df.groupby("category")["revenue_usd"].mean(), data=df, errorbar=("ci", False))
sns.barplot(x="category", y="revenue_usd", data=avg_df, errorbar=("ci", False))
plt.show()

"""
2.  Build a scatter plot to visualize the relationship between the number of items in an order (units_sold) and 
    the revenue (revenue_usd):
    Set the marker size to 100 units for better clarity by adding the parameter s=100.
    What can be said about the nature of the relationship between the number of items in an order and the revenue?
    Add the product category as a color on the scatter plot:
    Choose the "deep" palette for this.
    Are there differences between categories on this chart? How would you describe them?
"""
#sns.scatterplot(data=tips, x="total_bill", y="tip", hue="size", palette="viridis", size="size", sizes=(20, 200))

sns.scatterplot(data=df, x="revenue_usd", y="units_sold", s=100, hue="traffic_source", palette="deep", size="traffic_source", sizes=(10, 100))
plt.title("Revenue vs Units Sold")
plt.xlabel("Revenue ($)")
plt.ylabel("Units Sold")
plt.show()
