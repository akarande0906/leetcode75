'''
Leetcode 167: Two Sum II - Input Array is Sorted
'''
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lptr, rptr = 0, len(numbers) - 1
        while lptr < rptr:
            if numbers[lptr] + numbers[rptr] == target:
                return [lptr+1, rptr+1]
            elif numbers[lptr] + numbers[rptr] > target:
                # Need to reduce rptr
                rptr -= 1
            else:
                # Increase lptr as we are lesser than target
                lptr += 1
        return []
    
twoSum = Solution().twoSum
print (twoSum([1,2,3,4], 3))
print (twoSum([2,7,11,15], 9))
print (twoSum([2,3,4], 6))
print (twoSum([-1,0], -1))
        