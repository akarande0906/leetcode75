'''
Leetcode 189: Rotate Array
'''

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(start, end):
            left, right = start, end
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        n = len(nums)
        reverse(0, n - 1) # First reverse all elements
        reverse(0, k - 1) # Now reverse the first k elements
        reverse(k, n - 1) # Now reverse the remaining elements
    
        print(nums)

rot = Solution().rotate
rot([1,2,3,4,5,6,7], 3)
rot([-1,-100,3,99], 2)