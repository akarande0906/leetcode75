'''
Leetcode 287: Find the Duplicate Number
'''
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Negate the index of each element we encounter
        # If we encounter a negative element it means
        # We found a duplicate
        for num in nums:
            id = abs(num) - 1
            if nums[id] < 0:
                return abs(num)
            else:
                # Negate the number at the expected id
                nums[id] = -nums[id]
        return 0

dup = Solution().findDuplicate
print(dup([1,3,4,2,2]))
print(dup([3,1,3,4,2]))
print(dup([3,3,3,3,3]))
