'''
Leetcode 268: Missing Number
'''
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actual_sum = sum(nums)
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        return expected_sum - actual_sum
    
    # Slight variation where we start the range from 1 instead of 0
    def missingNumber2(self, nums: List[int]) -> int:
        actual_sum = sum(nums)
        n = len(nums) + 1 # We add 1 because the range is 1 to n and one number is missing
        expected_sum = n * (n + 1) // 2
        return expected_sum - actual_sum

misser = Solution().missingNumber
print(misser([3,0,1]))
print(misser([0,1]))
print(misser([9,6,4,2,3,5,7,0,1]))

misser = Solution().missingNumber2
print(misser([3,4,1]))
print(misser([1,3]))
print(misser([9,6,4,2,3,5,7,1]))