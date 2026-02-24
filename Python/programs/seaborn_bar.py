import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset("tips")
"""
# Seaborn bar plot
sns.barplot(data=tips, x="day", y="tip", errorbar=("ci", False))
#sns.barplot(data=tips, x="day", y="tip")
plt.title("Average Tips by Day")
plt.xlabel("Day")
plt.ylabel("Average Tips")
plt.show()


# Seaborn complex bar plot
sns.barplot(data=tips, x="day", y="tip", hue="time", errorbar=("ci", False))
plt.title("Average Tips by Day and Time")
plt.xlabel("Day")
plt.ylabel("Average Tips")
plt.show()
"""

# Seaborn scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="size", palette="viridis", size="size", sizes=(20, 200))
plt.title("Total Bill vs Tip (Seaborn)")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()

