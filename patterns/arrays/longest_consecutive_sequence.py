'''
Leetcode 128: Longest Consecutive Sequence
'''
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # First we put the numbers in a set to find later
        num_set = set(nums)
        max_len = 0
        for num in nums:
            # We need to see if the number is the beginning of a sequence 
            # and continue to iterate till we run out of elements
            if not num - 1 in num_set:
                # This number is the beginning of a sequence
                cur, cur_len = num, 0
                while cur in num_set:
                    cur += 1
                    cur_len += 1
                max_len = max(max_len, cur_len)
        return max_len
    
longestSeq = Solution().longestConsecutive
print(longestSeq([2,20,4,10,3,4,5]))
print(longestSeq([0,3,2,5,4,6,1,1]))
print(longestSeq([100,4,200,1,3,2]))
print(longestSeq([0,3,7,2,5,8,4,6,0,1]))

