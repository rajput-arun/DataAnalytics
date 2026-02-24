nums = [3,4,1,2,4]
for num in nums[:]:
    if num==4:
        nums.remove(num)
print(nums)

for i in range(3):
    if i == 1:
        pass
    print(i, end=" ")
