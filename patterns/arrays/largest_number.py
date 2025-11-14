'''
Leetcode 179: Largest Number
'''
from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num_strs = list(map(str, nums))
        # Custom sort to ensure numbers like 3 are larger before 30 or 32 
        num_strs.sort(key=lambda x: x*10, reverse=True)
        if num_strs[0] == '0':
            return '0'
        largest = ''.join(num_strs)
        return largest
    
    def largestNumber_comp(self, nums: List[int]) -> str:
        num_strs = list(map(str, nums))
        def cmp(a, b):
            if a+b > b+a:
                return -1
            elif a+b < b+a:
                return 1
            return 0
        num_strs.sort(key=cmp_to_key(cmp))
        if num_strs[0] == '0':
            return '0'
        largest = ''.join(num_strs)
        return largest
    
largest = Solution().largestNumber
print(largest([10,2]))
print(largest([3,30,34,5,9]))