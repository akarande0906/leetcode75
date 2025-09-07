class Solution:
    def maxSubArray(self, nums: list[int]) -> int:        
        newNum = maxTotal = nums[0]        
        
        for i in range(1, len(nums)):
	    # Resets start of the current newNum is negative
            newNum = max(nums[i], nums[i] + newNum)
            maxTotal = max(newNum, maxTotal)

        return maxTotal	


sol = Solution()
print (sol.maxSubArray([1]))
print (sol.maxSubArray([-1,-2]))
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(sol.maxSubArray([-1,2]))
