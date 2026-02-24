import matplotlib.pyplot as plt
# Sales data by region
regions = ["North", "South", "East", "West"]
sales = [300, 450, 200, 500]

plt.bar(regions, sales, color="skyblue")
plt.title("Sales by Region")  # Title of the graph
plt.xlabel("Regions")  # X-axis label
plt.ylabel("Sales")  # Y-axis label
plt.show()

plt.barh(regions, sales, color="skyblue")
plt.title("Sales by Region")  # Title of the graph
plt.xlabel("Sales")  # X-axis label
plt.ylabel("Regions")  # Y-axis label
plt.show()
