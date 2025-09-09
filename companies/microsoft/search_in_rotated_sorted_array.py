'''
Leetcode 33: Search in Rotated Sorted Array
'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[right]:
                if nums[right] >= target and nums[mid] < target:
                    # Is means this is in its place and not rotated
                    left = mid + 1
                else: # THis means that this portion of the array is rotated
                    right = mid - 1
            else:
                if nums[left] <= target and nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1 
    
search = Solution().search
print(search([4,5,6,7,0,1,2], 0))
print(search([4,5,6,7,0,1,2], 3))
print(search([1], 0))