def count_letters_in_string(string: str) -> dict:
    result = {}
    char_array=()
    string = string.lower()
    for chars in string:
        if chars in result:
            result[chars] += 1
        else:
            result[chars] = 1
    #print(sorted(result.items()))
    print(dict(sorted(result.items())))
    return (dict(sorted(result.items())))

count_letters_in_string("aalpaashSabsetsTs")
