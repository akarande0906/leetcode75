'''
Leetcode 283: Move Zeros
'''
# Modify the array in place
from typing import List

class Solution:
    def moveZeros(self, nums: List[int]) -> None:
        zeros = 0
        pointer = 0
        lng = len(nums)
        # Move all non-zero elements to the left
        for i in range(lng):
            if nums[i] == 0:
                zeros += 1
            else: 
                nums[pointer] = nums[i]
                pointer += 1
        # Now fill all the zeros at the end
        for i in range(lng-1, lng-zeros-1, -1):
            nums[i] = 0
        print (nums)

Solution().moveZeros([0,1,0,3,12]) 
Solution().moveZeros([0]) 
Solution().moveZeros([1,0,2,0,3,0,-4,0]) 