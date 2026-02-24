def get_leaders(numbers: list) -> list:
    leaders = []
    ln = len(numbers)
    j=1
    for number in numbers:
        chk = 0
        for i in range(j, ln):
            chk += numbers[i]
            #print(f"number[{i}]: {numbers[i]}, chk: {chk}")
            if chk > number:
                break
        #print(chk)
        if number > chk:
            leaders.append(number)
        j+=1
    #print(leaders)
    return(leaders)


get_leaders([21, 9, 1, 3, 2, 2])
#get_leaders([16, 17, 4, 3, 5, 2])
#== [17, 5, 2])

# 17 is greater than the sum of all elements to its right.
# 5 is greater than the sum of all elements to its right.
# The last element 2 is greater than the sum of its right elements.


