import matplotlib.pyplot as plt


days= ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
visitors= [120, 150, 130, 170, 200, 230, 180]

for x, y in zip(days, visitors):
    plt.text(x, y, f"{y:.0f}", ha="center", va="bottom", color="red")

plt.plot(days,visitors,label="No. of Visitors", marker="o", color="blue")
plt.xlabel("Days")
plt.ylabel("Visitors")
plt.show()