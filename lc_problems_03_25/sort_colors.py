'''
LC 75: Sort Colors
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent
'''
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Count the number of 0s, 1s and 2s and place them in the array
        zero_count, one_count, two_count = 0, 0, 0
        for n in nums:
            if n == 0:
                zero_count += 1
            elif n == 1:
                one_count += 1
        two_count = len(nums) - zero_count - one_count
        i = 0
        while i < len(nums):
            if zero_count:
                nums[i] = 0
                zero_count -= 1
            elif one_count:
                nums[i] = 1
                one_count -= 1
            else:
                nums[i] = 2
                two_count -= 1
            i += 1
        print (nums)
        
            
# TC : O(n)
# SC : O(1)
sortColors = Solution().sortColors
sortColors([2,0,2,1,1,0])
sortColors([2,0,1])
sortColors([0])
sortColors([2,1,2,1,1,1,2])
