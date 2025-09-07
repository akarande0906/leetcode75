class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        msum = -10**4 - 1
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum > msum: 
                    msum = sum
        return msum

sol = Solution()
print (sol.maxSubArray([1]))
print (sol.maxSubArray([-1,-2]))
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(sol.maxSubArray([-1,2]))
