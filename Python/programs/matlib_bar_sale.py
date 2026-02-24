import matplotlib.pyplot as plt


products= ["Product A", "Product B", "Product C", "Product D"]
sales= [400, 300, 500, 600]

plt.bar(products, sales, color="skyblue")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()

plt.barh(products, sales, color="skyblue")
plt.xlabel("Sales")
plt.ylabel("Products")
plt.show()
