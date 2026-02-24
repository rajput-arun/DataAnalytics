"""
Create a histogram to visualize the distribution of sales prices (sales).
Analyze which sales are most common and the overall nature of the value distribution.

Create a line chart to show the change in sales (sales) over time (order_date).
First, ensure that the order_date column has the appropriate data type. This will help
identify trends in purchases over the specified period. What is the trend according to the chart?

Build a bar chart to display the number of orders by product categories (product_category).
Use data grouping. Which category is the most popular? Which is the least popular?

Create a scatter plot to visualize the relationship between profit (profit) and total sales (sales).
Consider whether there is a correlation between these indicators and the nature of the relationship.

Create a grid of charts (2x2) from the previous visualizations to view all the charts on a single
figure and compare them.

"""
from xmlrpc.server import list_public_methods

import matplotlib.pyplot as plt
#import numpy as np
import pandas as pd
#from matplotlib.lines import lineMarkers

fpath = "g:/My Drive/Data Analyst/Python/data/"
# import CSV file
ds = pd.read_csv(fpath+"sales_data_updated.csv")
ds.head()
print(ds)

fig, ax = plt.subplots(2,2, figsize=(20,8))

pivot_sales = ds.pivot_table(index="order_date", values="sales", aggfunc=["sum"])
print(pivot_sales)

ord_dates = ds["order_date"].unique()
day_sales = ds.groupby("order_date")["sales"].sum()

#Create a histogram to visualize the distribution of sales prices (sales).
# Chart 1 : Histogram (0,0)
ax[0,0].hist(day_sales, color="grey")
ax[0,0].set_title("Daily Sales Analysis")
ax[0,0].set_xlabel("Order Date")
ax[0,0].set_ylabel("Sales")

#Create a line chart to show the change in sales (sales) over time (order_date).
# Chart 2: Line Chart

(
    ds
    .groupby("order_date", observed=False)["sales"].sum()
    .plot(kind="line", ax=ax[0,1], color="blue")
)

ax[0,1].set_title("Sales distribution over period")
ax[0,1].set_xlabel("Order Date")
ax[0,1].set_ylabel("Sales")

#Build a bar chart to display the number of orders by product categories (product_category).
prod_cat = ds["product_category"].unique()
prod_sales = ds.groupby("product_category")["sales"].sum()
print(prod_sales)

ax[1,0].bar(prod_cat, prod_sales, color="lightblue")
ax[1,0].set_title("Sales per category")
ax[1,0].set_xlabel("Product Category")
ax[1,0].set_ylabel("Sales")

#Create a scatter plot to visualize the relationship between profit (profit) and total sales (sales).
ax[1,1].scatter(ds["sales"],ds["profit"],alpha=0.1, color="green")
ax[1,1].set_title("Profit Vs. Sales")
ax[1,1].set_xlabel("Sales")
ax[1,1].set_ylabel("Profit")

plt.show()
