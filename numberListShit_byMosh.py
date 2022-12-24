# Removes duplicates from list
scrotum = [2, 2, 3, 1, 9, 139, 4, 2, 3, 4, 5, 1, 2, 3]
print(scrotum)
x=[]
for i in scrotum:
    if i not in x:
        x.append(i)
print(x)

# Find max value in list
def find_max(nums):    
    max = nums[1]
    for i in nums:
        if i > max:
            max = i
    return max
    
print(f"Max number is {find_max(scrotum)}")
