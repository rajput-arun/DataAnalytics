import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt

# Sales data over 5 months
tips = sns.load_dataset("tips")

days=tips["day"].unique()
print(days)

time_of_day=tips["time"].unique()
print(time_of_day)

day_tips=tips.groupby("day", observed=True)["tip"].sum()
print(day_tips)

time_tips=tips.groupby("time", observed=True)["tip"].sum()
print(time_tips)

months = ["January", "February", "March", "April", "May"]
sales = [150, 200, 300, 250, 400]

plt.plot(days,  day_tips, marker="o", linestyle="-", color="blue")
#plt.plot(time_of_day, time_tips, marker="o", linestyle="-", color="blue")
plt.title("day wise tips ")  # Title of the graph
plt.xlabel("days")  # X-axis label
plt.ylabel("tips")  # Y-axis label
plt.show()
