import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

avg_tip = tips.groupby("day", observed=True).tip.mean()
#avg_tip = tips.groupby(["day"], observed=True).mean()
print(avg_tip)

plt.scatter(tips["total_bill"], tips["tip"], color="green", alpha=0.5)
plt.title("Total Bill vs. Tip")  # Title of the graph
plt.xlabel("Total Bill ($)")  # X-axis label
plt.ylabel("Tip ($)")  # Y-axis label
plt.show()
