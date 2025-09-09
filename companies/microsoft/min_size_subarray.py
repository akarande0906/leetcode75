'''
Leetcode 209: Minimum Size Subarray Sum
'''
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur_sum, min_size = 0, float('inf')
        left = 0
        for right in range(len(nums)):
            cur_sum += nums[right]
            if cur_sum >= target:
                while cur_sum >= target:
                    min_size = min(min_size, right - left + 1)
                    cur_sum -= nums[left]
                    left += 1
        return min_size if min_size != float('inf') else 0
                
array_len = Solution().minSubArrayLen
print (array_len(7, [2,3,1,2,4,3]))
print (array_len(4, [1,4,4]))
print (array_len(11, [1,1,1,1,1,1,1,1]))
print (array_len(7, [1,1,1,1,1,1,1,1]))
print (array_len(11, [1,2,3,4,5]))

