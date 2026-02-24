import matplotlib.pyplot as plt
import pandas as pd

"""
import seaborn as sns
tips = sns.load_dataset("tips")
plt.scatter(tips["total_bill"], tips["tip"], color="green", alpha=0.5)
plt.title("Total Bill vs. Tip")  # Title of the graph
plt.xlabel("Total Bill ($)")  # X-axis label
plt.ylabel("Tip ($)")  # Y-axis label
plt.show()
"""

fpath = "g:/My Drive/Data Analyst/Python/data/"
# import CSV file
ds = pd.read_csv(fpath+"sales_data_updated.csv")
ds.head()
print(ds)

plt.scatter(ds["sales"], ds["profit"], color="green", alpha=0.5)
plt.title("Sales vs. Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()

