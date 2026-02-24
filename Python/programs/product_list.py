"""
Create a function product_list that:

Takes a list of numbers, where:
Input list contains at least 2 elements.
List contains only positive numbers.
Numbers can be repeated.
Returns a list of the same size, where:
Each element is the product of all other elements in the list.
Example 1:

product_list([1, 5, 2]) == [10, 2, 5]

# The first element 10 is the product of all elements except 1
# The second element 2 is the product of all elements except 5
# The third element 5 is the product of all elements except 2

Example 2:

product_list([12, 20]) == [20, 12]

# The first element 20 is the product of all elements except 12
# The second element 12 is the product of all elements except 20

"""


def product_list(numbers: list) -> list:
    final_list = []
    curr_pos = 0
    ln = len(numbers)
    product = 1
    for number in numbers:
        for i in range (0, ln):
            if i != curr_pos:
                product *= numbers[i]
        curr_pos += 1
        final_list.append(product)
        product = 1
    print (final_list)
    return final_list



product_list([12, 20])
