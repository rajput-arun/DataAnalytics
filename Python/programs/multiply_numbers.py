def multiply_numbers(*args, **kwargs):
    # Case 1: positional arguments exist
    if args:
        if len(args) == 1:
            return args[0]
        return args[0] * args[1]

    # Case 2: only keyword arguments exist
    if kwargs:
        result = 1
        for value in kwargs.values():
            result *= value
        return result

    # Case 3: nothing passed
    return 1


print(multiply_numbers()) #== 1
print(multiply_numbers(2, 3)) # == 6
print(multiply_numbers(b=5)) #== 5
print(multiply_numbers(4, 3, "string", [])) #== 12
print(multiply_numbers(1, 3, "string", k=22)) #== 3
