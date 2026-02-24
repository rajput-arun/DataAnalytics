def row_weights(row: list) -> list:
    weights=[0,0]
    i=1
    #print(weights)
    for n in row:
        d = i % 2
        #weights.append(d)
        weights[d] += n
        i += 1
    print(f"sum of odd positioned values : {weights[1]}")
    print(f"sum of even positioned values: {weights[0]}")
    return (weights[1],weights[0])


row_weights ([1,8,5,5,6,7])