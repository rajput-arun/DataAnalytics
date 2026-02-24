rng=int(input("Enter range: "))
prime_nums=[]
for i in range(1, rng+1):
    Prime = True
    for j in range(2, i+1):
        if (i != j and i % j == 0):
            Prime = False
            break
    if Prime:
        prime_nums.append(i)

print(prime_nums)
print(len(prime_nums))

