class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums[1] = max(nums[0], nums[1])
        for house in range(2, len(nums)):
            nums[house] = max(nums[house] + nums[house - 2], nums[house - 1])
        return nums[-1]

print(Solution().rob([1,2,3,1]))
print(Solution().rob([2,7,9,3,1]))
print(Solution().rob([2,1,2,10,1]))
