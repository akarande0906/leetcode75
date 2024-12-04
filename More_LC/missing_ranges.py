'''
LC 163: Missing Ranges
You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are within the inclusive range.
A number x is considered missing if x is in the range [lower, upper] and x is not in nums.
Return the shortest sorted list of ranges that exactly covers all the missing numbers. 
That is, no element of nums is included in any of the ranges, and each missing number is covered by one of the ranges.
Input: nums = [0,1,3,50,75], lower = 0, upper = 99 Output: [[2,2],[4,49],[51,74],[76,99]]
Explanation: The ranges are:[2,2] [4,49] [51,74] [76,99]
'''
class Solution:
    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        prev_min = lower - 1
        output_array = []
        if not nums:
            return [[lower, upper]]
        for i in range(len(nums)):
            if prev_min < nums[i] and nums[i] - prev_min > 1:
                output_array.append([prev_min + 1, nums[i] - 1])
            prev_min = nums[i]
        if nums[len(nums) - 1] < upper:
            output_array.append([nums[len(nums) - 1]  + 1, upper])
        return output_array

ranger = Solution().findMissingRanges
print (ranger([1,2,3,50,75], 0, 99))
print (ranger([-1], -1, -1))
print (ranger([0,1,3,50,75], 0, 99))
print (ranger([], 0, 99))