"""
rotate array from given position

eg. [1,2,3,4,5,6,7,8,9]
k = 4

returns [6,7,8,9,1,2,3,4,5]

"""

arr = [1,2,3,4,5,6,7,8,9]
rot_arr=[]
k=7
print(arr)
for i in range (k, len(arr)):
    rot_arr.append(arr[i])

for num in range (0, k):
    rot_arr.append(arr[num])

print(rot_arr)
