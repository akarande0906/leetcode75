'''
LC 75: Sort Colors
'''
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Count the number of 0s, 1s and 2s and place them in the array
        zero_count, one_count, two_count = 0, 0, 0
        for n in nums:
            if n == 0:
                zero_count += 1
            elif n == 1:
                one_count += 1
        two_count = len(nums) - zero_count - one_count
        i = 0
        while i < len(nums):
            if zero_count:
                nums[i] = 0
                zero_count -= 1
            elif one_count:
                nums[i] = 1
                one_count -= 1
            else:
                nums[i] = 2
                two_count -= 1
            i += 1
        print(nums)
        
            
# Time Complexity: O(n) where n is the length of the input list.
# Space Complexity: O(1) since we are not using any extra space other than a few variables.

sol = Solution()
sol.sortColors([2,0,2,1,1,0])  # [0,0,1,1,2,2]
sol.sortColors([2,0,1])        # [0,1,2]
sol.sortColors([0])            # [0]
sol.sortColors([2,1,2,1,0,1,2,0])