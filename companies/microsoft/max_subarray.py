'''
Leetcode 53: Maximum Subarray Sum
'''
from typing import List

# Kadane's algorithm: We reset the cur_sum if the sum is less than 0
# Each time we compare the max sum with the current sum and update as needed.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int: 
        cur_sum, max_sum = 0, 0
        for n in nums:
            # cur_sum = max(n, cur_sum + n)
            # max_sum = max(cur_sum, max_sum)
            cur_sum = cur_sum + n
            if cur_sum < 0:
                cur_sum = 0
            max_sum = max(max_sum, cur_sum)
        return max_sum

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(Solution().maxSubArray([1]))
print(Solution().maxSubArray([5,4,-1,7,8]))