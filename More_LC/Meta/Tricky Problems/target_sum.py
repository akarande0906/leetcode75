'''
LC 494: Target Sum
You are given an integer array nums and an integer target.
You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.
Input: nums = [1,1,1,1,1], target = 3 Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
'''
class Solution:
    ''' Brute Force: TC 2^n   SC: O(n) : Depth of tree'''
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        self.total_count = 0
        def backtrack(current_sum, offset):
            if offset == len(nums):
                if current_sum == target:
                    self.total_count += 1
                return
            backtrack(current_sum - nums[offset], offset + 1)
            backtrack(current_sum + nums[offset], offset + 1)
        backtrack(0, 0)
        return self.total_count
    
    ''' With Memoization: TC: O(n*s) where s is the sum of elements in the array SC: O(n*s) since we store 2D array of n*s'''
    def findTargetSumWaysMemo(self, nums: list[int], target: int) -> int:
        self.total_count = 0
        memo = {}
        def backtrack(current_sum, offset):
            if offset == len(nums):
                if current_sum == target:
                    return 1
                return 0
            # Check cache
            if (offset, current_sum) in memo:
                return memo[(offset, current_sum)]
            decrement = backtrack(current_sum - nums[offset], offset + 1)
            increment = backtrack(current_sum + nums[offset], offset + 1)
            memo[(offset, current_sum)] = decrement + increment
            return decrement + increment 
        return backtrack(0, 0)
       

print (Solution().findTargetSumWays([1,1,1,1,1], 3))