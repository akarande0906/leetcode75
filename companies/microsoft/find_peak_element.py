'''
Leetcode 162: Find Peak Element
'''
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]: # This could be a peak, but we check left
                right = mid
            else:
                left = mid + 1
        return left
    
pk_finder = Solution().findPeakElement
print(pk_finder([1,2,3,1]))
print(pk_finder([1,2,1,3,5,6,4]))
print(pk_finder([1,4,3,2,1,5,6,7,8]))