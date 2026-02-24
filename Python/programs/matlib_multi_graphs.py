from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

#fig, ax = plt.subplots(1,2,figsize=(10,5))
#plt.show()


# Generate random e-commerce data
np.random.seed(42)
data = {
    "product": ["Product A", "Product B", "Product C", "Product D"],
    "sales": np.random.randint(100, 500, size=4),
    "profit": np.random.randint(10, 100, size=4),
}

print(data)
# Create a DataFrame
df = pd.DataFrame(data)

# Create a figure with 1 row and 2 columns of subplots
fig, ax = plt.subplots(1, 2, figsize=(10, 4))

# First subplot - Bar plot
ax[0].bar(df["product"], df["sales"], color="blue")
ax[0].set_title("Sales Over Products")  # Title of the subplot
ax[0].set_xlabel("Product")  # X-axis label
ax[0].set_ylabel("Sales ($)")  # Y-axis label

# Second subplot - Bar plot
ax[1].bar(df["product"], df["profit"], color="green")
ax[1].set_title("Profit Over Products")  # Title of the subplot
ax[1].set_xlabel("Product")  # X-axis label
ax[1].set_ylabel("Profit ($)")  # Y-axis label

# Adjust layout
plt.tight_layout()

# Show plots
plt.show()
