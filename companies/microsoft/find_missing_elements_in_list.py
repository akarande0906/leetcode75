'''
Leetcode 448: Find All Numbers Disappeared in Array
'''
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        temp_array = [0] * len(nums)
        return_array = []
        for i in range(len(nums)):
            temp_array[nums[i] - 1] = 1
        for i in range(len(temp_array)):
            if not temp_array[i]:
                return_array.append(i+1)
        return return_array
    # Time Complexity: O(n), Space Complexity: O(n) for temp_array


    def findDisappearedNumbers_O_1_s(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):
            cur_index = abs(nums[i]) - 1
            if nums[cur_index] > 0:
                nums[cur_index] *= -1 # negate the number at the intended position
        # Now iterate over the array and find all non negative elements
        # The positions will indicate which numbers are missing
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i+1)
        return result 
    # Time Complexity: O(n), Space Complexity: O(1)
        
finder = Solution().findDisappearedNumbers
print(finder([4,3,2,7,8,2,3,1]))
print(finder([1,1]))

finder = Solution().findDisappearedNumbers_O_1_s
print(finder([4,3,2,7,8,2,3,1]))
print(finder([1,1]))