import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset("tips")
print(tips)

bill_pivot=pd.pivot_table(tips,values="total_bill",index="day",columns="time", aggfunc=["count","sum"], fill_value=0, observed="total_bill")
print(bill_pivot)

plt.hist(tips["total_bill"], bins=10)
plt.title("Distribution of Total Bills")  # Title of the histogram
plt.xlabel("Total Bill ($)")  # X-axis label
plt.ylabel("Frequency")  # Y-axis label
plt.show()

plt.hist(tips["total_bill"], bins=10)
plt.title("Distribution of Total Bills")  # Title of the histogram
plt.xlabel("Total Bill ($)")  # X-axis label
plt.ylabel("Frequency")  # Y-axis label

xval=plt.gca().get_xlim()
yval=plt.gca().get_ylim()
print(f"x(1, 2): {round(xval[0],0)}, {round(xval[1],0)}")
print(f"y(1, 2): {round(yval[0],0)}, {round(yval[1],0)}")

x_ticks = np.arange(0, tips["total_bill"].max() + 2, 2)
plt.xticks(x_ticks)

y_ticks = np.arange(0, plt.gca().get_ylim()[1] + 5, 5)
plt.yticks(y_ticks)

plt.show()
