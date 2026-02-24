"""
Create a histogram to visualize the distribution of profit (profit). Analyze the overall nature
of the distribution and which values are most common.

Build separate histograms of profit for sales made via web browser and mobile app (device_type).
Create this visualization both on a single chart (using the hue parameter) and on separate
charts (using the col parameter). Use Google or ChatGPT to learn how the col parameter works.

Create a line chart showing the change in profits (profit) over time (order_date). Before
plotting, ensure the order_date column has the correct data type. This will help identify
trends in purchases over the given period. What is the trend according to the chart?
Write your answer in a text block.

Build a bar chart showing total profit by product category (product_category). Which
category is the most profitable? Which is the least profitable? Write your answer
in a text block.

Use the hue parameter and the gender column to compare total profits by category for
male and female customers. What conclusions can be drawn? Are there differences in
behavior between the two customer groups? Write your answer in a text block.

"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

fpath = "g:/My Drive/Data Analyst/Python/data/"
# import CSV file
df = pd.read_csv(fpath+"sales_data_updated.csv")
import pandas as pd
df["order_date"] = pd.to_datetime(df["order_date"])
df.head()

print(df, sep)

"""
Create a histogram to visualize the distribution of profit (profit). Analyze the overall nature
of the distribution and which values are most common.
"""
sns.histplot(data=df, x="profit")
plt.title("Histogram of profit for sales")
plt.xlabel("Profit")
plt.ylabel("Customers")
plt.show()


"""
Build separate histograms of profit for sales made via web browser and mobile app (device_type).
Create this visualization both on a single chart (using the hue parameter) and on separate
charts (using the col parameter). Use Google or ChatGPT to learn how the col parameter works.
"""

sns.histplot(data=df,
    x="profit",
    hue="device_type",
    bins=30,
    element="step",
    stat="density",
    common_norm=False
)
plt.title("Profit distribution by device type")
plt.xlabel("Profit")
plt.ylabel("Customers")
plt.show()

"""
Create a line chart showing the change in profits (profit) over time (order_date). Before
plotting, ensure the order_date column has the correct data type. This will help identify
trends in purchases over the given period. What is the trend according to the chart?
Write your answer in a text block.
"""

sns.lineplot(data=df, x="order_date", y="profit")
plt.title("Profit distribution by order date")
plt.xlabel("Order Date")
plt.ylabel("Profit")
plt.show()

"""
Build a bar chart showing total profit by product category (product_category). Which
category is the most profitable? Which is the least profitable? Write your answer
in a text block.
"""

sns.barplot(data=df, x="product_category", y="profit", hue="device_type", palette="deep")
plt.title("Total profit by product category")
plt.title("Profit distribution by product category")
plt.xlabel("Product Category")
plt.ylabel("Profit")
plt.show()
