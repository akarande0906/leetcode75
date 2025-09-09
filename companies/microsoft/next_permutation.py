'''
Leetcode 31: Next Permutation of array
'''
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> List[int]:
        # First we find the pivot: The pivot is the first non increasing element iterating from the right
        # Then we swap this with the element that is the next greatest with respect to pivot to the right
        # Finally we reverse elements to the right of the pivot
        # E.g. [3, 4, 2, 1] => Pivot is 3, next largest element is 4, we swap these two: [4, 3, 2, 1]        
        # Then we reverse the elements to the right of the pivot : [4, 1, 2, 3]

        pivot = -1
        for n in range(len(nums) - 2, 0, -1):
            if nums[n-1] < nums[n]:
                pivot = n-1
                break
        if pivot == -1: # If this was the last permutation, we cycle
            nums.reverse()
        else:    
            # Now find the element to swap with
            max_id, max_elem = -1, float('inf')

            for n in range(pivot + 1, len(nums)):
                if nums[n] > nums[pivot] and nums[n] <= max_elem:
                    max_elem = nums[n]
                    max_id = n
            nums[pivot], nums[max_id] = nums[max_id], nums[pivot]

            # Finally reverse elements to the right of pivot
            nums[pivot+1::] = nums[pivot+1::][::-1]

        print (nums)

    
perm_fun = Solution().nextPermutation
perm_fun([3,4,2,1])

# Time Complexity: O(n), Space Complexity: O(1) - In place

