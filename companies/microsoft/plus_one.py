'''
Leetcode 66: Plus One
'''
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9: # It means this can be incremented and we can return the array
                digits[i] += 1
                return digits
            # If we encounter a 9, we need to reset this to 0
            digits[i] = 0
        # If we got this far then the left most digit was a 9 and that means we need to carry forward a 1
        return [1] + digits

p_one = Solution().plusOne
print(p_one([1,2,3]))
print(p_one([4,3,2,1]))
print(p_one([9,9,0]))
print(p_one([9,9]))
