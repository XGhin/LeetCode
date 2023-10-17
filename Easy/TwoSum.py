class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                temp = nums[i] + nums[j]
                if temp == target:
                    print("({}), ({})".format(i, j))
                    return i, j