import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

day_tips = tips["day"].unique()
avg_tip = tips.groupby("day", observed=True).tip.mean()
#avg_tip = tips.groupby(["day"], observed=True).mean()
print(avg_tip)
print(day_tips)

plt.bar(day_tips, avg_tip)
plt.title("Average Tip per Day")
plt.xlabel("Day of Week")
plt.ylabel("Average Tips")
plt.show()

"""
plt.scatter(tips["total_bill"], tips["tip"], color="green", alpha=0.5)
plt.title("Total Bill vs. Tip")  # Title of the graph
plt.xlabel("Total Bill ($)")  # X-axis label
plt.ylabel("Tip ($)")  # Y-axis label
plt.show()
"""