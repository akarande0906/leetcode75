'''
Leetcode 26: Remove Duplicates from Sorted Array
'''
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left_ptr, cur_val = 0, nums[0]
        for right_ptr in range(len(nums)):
            if nums[right_ptr] == nums[left_ptr]:
              continue
            else:
                left_ptr += 1
                nums[left_ptr] = nums[right_ptr]
        print (nums[0:left_ptr+1])
        return left_ptr + 1
    
print(Solution().removeDuplicates([1,1,2]))
print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
