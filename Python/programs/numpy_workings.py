import numpy as np

"""
# Creating a 2-D array with 2 rows and 2 columns
int_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=np.int8)
#print(int_array)
ad_clicks = np.array(np.random.randint(60,10001,size=60, dtype=np.uint16))
#print(ad_clicks)

char_array = np.array(["a", "b", "c", "d", "e", "f", "g", "h", "i"], dtype=object)
mrg_array = np.concatenate((int_array, char_array), axis=0)
# types of elements
int_array.dtype
char_array.dtype
mrg_array.dtype

my_array = np.array(range(0, 11,1), dtype=np.uint8)
tp=type(my_array)
#print(f"type : {tp}")
print(f"\n{my_array} \n")
print(f"my_array[2:6]: {my_array[2:6]}") # elements from 3rd to 6th
print(f"my_array[:5]: {my_array[:5]}") # first 5 elements
print(f"my_array[-3:]: {my_array[-3:]}") # last 3 elements
print(f"my_array[1:7:2]: {my_array[1:7:2]}") # elements from second to seventh with a step of 2
print(f"my_array[:8:3]: {my_array[:8:3]}") # elements from the start of the array to the eighth with a step of 3
print(f"my_array[::-1]: {my_array[::-1]}") # array elements in reverse order


my_matrix = np.array(range(10, 121, 10)).reshape((3, 4)) # used the 'reshape' method to transform a vector into a matrix
print(my_matrix)

print(my_matrix[0, 0]) # element in the first row and first column
print(my_matrix[-1, 2]) # element in the last row and third column
print(my_matrix[:2, :2]) # elements of the first two rows and the first two columns

print(my_matrix[:, 0]) # whole first column
print(my_matrix[2, :]) # whole third row


#print(int_array)
#print(char_array)
#print (mrg_array)


first_matrix = np.array([[1, -2], [3.5, 4]])

#print(f"First matrix:\n{first_matrix}")

players_height = [171, 190, 182, 176, 169, 188, 180, 181, 188, 175]
number_of_tall_players = 0
for height in players_height:
    if height > 185:
        number_of_tall_players += 1
print(f"Number of tall players: {number_of_tall_players}")

print("Using np.array -->")
players_height=np.array(players_height)
tall_players = players_height > 185
print(players_height[tall_players].size)

print("Using np.array (multi dimensional) -->")

players = np.array([[101, 175, 80], [102, 181, 82], [103, 179, 75], [104, 185, 90], [105, 184, 79]])
print(f"all players :\n {players}")
tall = 180
heavy = 78
tall_players = players[:,1] >= tall
heavy_players = players[:,2] > heavy

print(f"tall players :\n {players[tall_players,0]}")
print(f"heavy players:\n {players[heavy_players,0]}")

"""
x = np.random.randint(1, 10, size=5)
print("log(x + 5) =", np.log(x + 5))
print("exp(x) =", np.exp(x))
print("cos(x)^2 + sin(x)^2 =", np.cos(x) ** 2 + np.sin(x) ** 2)

x = np.arange(4)  # works similarly to range(4)
print("x     =", x)
print("x + 5 =", x + 5)
print("x - 5 =", x - 5)
print("x * 2 =", x * 2)
print("x / 2 =", x / 2)

print("-2 * x + 5.5 =", -2 * x + 5.5)

big_array = np.random.rand(1000000)  # creating a big array of random numbers
#sum(big_array)
print(np.sum(big_array))

sales_amount = np.array([55, 85, 17, 92, 99, 34, 44, 26, 66, 98])  # an array of product sales
print(f"Average sales amount: {np.mean(sales_amount)}")  # using a function
print(f"Average sales amount: {sales_amount.mean()}")  # using a method
print(f"Median sales amount: {np.median(sales_amount)}")

np.random.seed(0)
random_matrix = np.random.randint(10, size=(3, 4))  # 3x4 random number matrix
print(random_matrix)
print(f"\nSum of all elements: {random_matrix.sum()}")
print(f"Sum of each column: {random_matrix.sum(axis=0)}")
print(f"Sum of each row: {random_matrix.sum(axis=1)}")


import sys

arr = [0] * 1000  # creating list with len = 1000 filled with 0
print(sys.getsizeof(arr))
print(sys.getsizeof(np.array(arr, dtype=np.int8)))
