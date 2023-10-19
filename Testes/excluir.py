nums = [3,2,2,3]
val = 3
numscert = []
for i in range(len(nums)):
    if nums[i] != val:
        numscert.append(nums[i])
print(numscert)
