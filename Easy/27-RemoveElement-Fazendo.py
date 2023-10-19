nums = [3,2,2,3]
val = 3
k = 0
i = 0
for num in nums:
    if num != val:
        k = k + 1
    else:
        nums[i] = "_"
    i += 1
print(nums)
print(k)