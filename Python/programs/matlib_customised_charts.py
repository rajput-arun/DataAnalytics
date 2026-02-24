import matplotlib.pyplot as plt
import pandas as pd

data = {
    "product": ["Product A", "Product B", "Product C", "Product D"],
    "sales": [350, 150, 500, 450],
}

# Create a DataFrame
df = pd.DataFrame(data)

print(plt.style.available)

# Set a style for the plot
plt.style.use("fivethirtyeight")

# Plot a bar chart
plt.bar(df["product"], df["sales"], color="lightblue")
plt.title("Sales of Different Products")  # Title of the chart
plt.xlabel("Product")  # X-axis label
plt.ylabel("Sales ($)")  # Y-axis label
plt.show()
