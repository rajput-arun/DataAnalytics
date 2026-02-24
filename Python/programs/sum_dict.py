"""
Create a function sum_dicts that:

Takes an unlimited number of dictionaries, where:
All dictionary values are integers.
Numbers in the dictionary can be positive or negative.
Returns a dictionary that combines all of them.
If keys match, their values are summed.
The function always returns a dictionary.
Example 1:

empty = {}
sum_dicts() == {}
sum_dicts(empty) == {}

Example 2:

first = {"a": 2, "b": 4}
second = {"a": 2, "b": 10}
third = {"d": -5}

sum_dicts(first) == {"a": 2, "b": 4}
sum_dicts(first, third) == {"a": 2, "b": 4, "d": -5}
sum_dicts(first, second, third) == {"a": 4, "b": 14, "d": -5}
"""

def sum_dicts(*dicts) -> dict:
    result = {}
    for d in dicts:
        if not isinstance(d, dict):
            raise TypeError("All arguments must be dictionaries")

        for key, value in d.items():
            if not isinstance(value, (int, float)):
                raise TypeError(f"Value for key '{key}' must be a number")

            result[key] = result.get(key, 0) + value

    print(result)
    return (result)


first = {"a": 2, "b": 4}
second = {"a": 2, "b": 10}
third = {"d": -5}

sum_dicts(first, second)
