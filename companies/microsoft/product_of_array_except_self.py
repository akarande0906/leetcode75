'''
Leetcode 238: Product of Array except Self
'''
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sums = [1] * n
        p = nums[0] # Left Product
        r = nums[-1] # Right Product
        
        # Calculate the left products
        for i in range(1, n):
            sums[i] *= p
            p *= nums[i]
        # Calculate the right products
        for i in range(n-2, -1, -1):
            sums[i] *= r
            r *= nums[i]

        return sums
    
prod = Solution().productExceptSelf
print(prod([1,2,3,4]))
print(prod([-1,1,0,-3,3]))
