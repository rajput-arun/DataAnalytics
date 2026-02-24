import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")

# Create a figure with 2 rows and 2 columns of subplots
fig, ax = plt.subplots(2, 2, figsize=(10, 8))

# First subplot - Scatter plot of total_bill vs tip
ax[0, 0].scatter(tips["total_bill"], tips["tip"], color="blue")
ax[0, 0].set_title("Tip vs Total Bill")  # Title of the subplot
ax[0, 0].set_xlabel("Total Bill ($)")  # X-axis label
ax[0, 0].set_ylabel("Tip ($)")  # Y-axis label

# Second subplot - Bar plot of average tip by day
#tips.groupby("day", observed=False)["tip"].mean().sort_values().plot(
#    kind="barh", ax=ax[0, 1], color="green"
#)
(
    tips
    .groupby("day", observed=False)["tip"]
    .mean()
    .sort_values()
    .plot(kind="barh", ax=ax[0, 1], color="green")
)

ax[0, 1].set_title("Average Tip by Day")  # Title of the subplot
ax[0, 1].set_xlabel("Average Tip ($)")  # X-axis label
ax[0, 1].set_ylabel("Day")  # Y-axis label

# Third subplot - Bar plot of average tip by time of the day
tips.groupby("time", observed=False)["tip"].mean().plot(kind="bar", ax=ax[1, 0], color="skyblue")
ax[1, 0].set_title("Average Tip by Time")  # Title of the subplot
ax[1, 0].set_xlabel("Time")  # X-axis label
ax[1, 0].set_ylabel("Average Tip ($)")  # Y-axis label

# Fourth subplot - Histogram of total_bill
ax[1, 1].hist(tips["total_bill"], bins=15, color="purple")
ax[1, 1].set_title("Total Bill Distribution")  # Title of the subplot
ax[1, 1].set_xlabel("Total Bill ($)")  # X-axis label
ax[1, 1].set_ylabel("Frequency")  # Y-axis label

# Adjust layout
plt.tight_layout()

# Show plots
plt.show()
