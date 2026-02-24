"""
Find Smaller Digits


Create a function find_smaller_digits(ls) that:

Takes a list of integers ls.
Returns a new list, where each element in the new list represents the count of numbers to the right of ls[i] smaller than ls[i].
Example 1:

ls = [5, 4, 3, 2, 1]
result_list = [4, 3, 2, 1, 0]
find_smaller_digits(ls) == result_list
"""

def find_smaller_digits(ls: list) -> list:
    smaller_digits = []
    ln = len(ls)
    j = 1
    for number in ls:
        ctr=0
        for i in range (j, ln):
            if number > ls[i]:
                ctr += 1
        smaller_digits.append(ctr)
        j += 1

    print(smaller_digits)
    return(smaller_digits)


ls = [1, 2, 0]
find_smaller_digits(ls)
# == result_list
