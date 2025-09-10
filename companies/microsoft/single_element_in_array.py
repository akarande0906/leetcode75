'''
Leetcode 540: Single Element in Sorted Array
'''
from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def isOdd(subarr):
            return subarr % 2 == 1

        n = len(nums)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # Check if this elem is single or double
            cur_val = nums[mid]
            if mid > 0 and nums[mid-1] == nums[mid]:
                # This means mid has a pair
                left_length = mid - left - 1
                right_length = right - mid
                if isOdd(left_length): 
                # We need to go left as the sub array with single element
                # is on the left
                    right = mid - 2
                else:
                    left = mid + 1
            elif mid < (n-1) and nums[mid+1] == nums[mid]:
                # This means mid has a pair
                left_length = mid - left
                right_length = right - mid - 1
                if isOdd(left_length): 
                # We need to go left as the sub array with single element
                # is on the left
                    right = mid - 1
                else:
                    left = mid + 2
            else:
                return nums[mid]
        return nums[left] if left >= 0 and left <= (n-1) else nums[right]
    

    # Simpler but O(n) Time complexity
    def singleNonDuplicate_On(self, nums: List[int]) -> int:
        singular = 0
        for num in nums:
            singular = singular ^ num
        return singular
    
# Time Complexity: O(log n), Space Complexity: O(n)
singler = Solution().singleNonDuplicate
print(singler([1,1,2,3,3,4,4,8,8]))
print(singler([3,3,7,7,10,11,11]))
print(singler([3]))
print(singler([3,11,11]))
print('')
singler = Solution().singleNonDuplicate_On
print(singler([1,1,2,3,3,4,4,8,8]))
print(singler([3,3,7,7,10,11,11]))
print(singler([3]))
print(singler([3,11,11]))