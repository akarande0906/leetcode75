'''
Leetcode 3201: Find the Max Length of Valid Subsequences
'''
from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        result = 0
        # There are 4 possibilities:
        # All numbers in the subseq are odd
        # All numbers in the subseq are even
        # All numbers are odd then even and so on
        # All numbers are even then odd and so on
        # So we need to check which of these patterns 
        count_even, count_odd, count_alternative = 0, 0, 0
        last_parity = -1
        for num in nums:
            parity = num % 2
            if parity == 0: # Even
                count_even += 1
            else:
                count_odd += 1
            if parity != last_parity:
                count_alternative += 1
                last_parity = parity
        return max(count_even, count_odd, count_alternative)
    
maxLen = Solution().maximumLength
print(maxLen([1,2,3,4]))
print(maxLen([1,2,1,1,2,1,2]))
print(maxLen([1,3]))
print(maxLen([5,4,3,2,1]))
print(maxLen([1,1,1,2,2,2,3,3,3]))
print(maxLen([2,1,2,1,1,2,3,3,3]))