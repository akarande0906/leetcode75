class Solution:
    # Kadane's algorithm
    def maxSubArray(self, nums: list[int]) -> int:
       maxSum = nums[0]
       total = 0

       for n in nums:
            if total < 0:
                total = 0 # reset when you reach a negative sum
            total += n
            maxSum = max(total, maxSum)

       return maxSum 

sol = Solution()
print (sol.maxSubArray([1]))
print (sol.maxSubArray([-1,-2]))
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(sol.maxSubArray([-1,2]))
