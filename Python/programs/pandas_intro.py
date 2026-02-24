"""
Intro to Panda
"""
import pandas as pd
list_of_numbers = [100, 200, 300, 400]
series_of_numbers = pd.Series(list_of_numbers)
print("-"*30)
print(series_of_numbers)
print(series_of_numbers.index)
print(series_of_numbers.values)
print("-"*30)
print(f"First element: {series_of_numbers[0]}")
print(f"\nElements from second to third:\n{series_of_numbers[1:3]}")
print(f"\nLast two elements:\n{series_of_numbers[-2:]}")
print("-"*30)

series_of_number_with_index = pd.Series(list_of_numbers, index=["a", "b", "c", "d"])
print(series_of_number_with_index)
print("-"*30)
print(f"Element with index 'b': {series_of_number_with_index['b']}")
print(f"\nElements with indices from 'a' to 'c':\n{series_of_number_with_index['a':'c']}")
print("-"*30)
"""
DataFrames
"""
data = {
    "product_name": ["Laptop", "Smartphone", "Keyboard", "Tablet", "Headphones", "Router", "PC"],
    "quantity": [1, 2, 1, 3, 1, 2, 4],
    "price": [1200, 800, 120, 300, 150, 200, 1300],
    "order_date": ["2024-07-01", "2024-07-03", "2024-07-05", "2024-07-07", "2024-07-09", "2024-07-10", "2024-07-02"],
}

sales_info = pd.DataFrame(data)
print(sales_info)
