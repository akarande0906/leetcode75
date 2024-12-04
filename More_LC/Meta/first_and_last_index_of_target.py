'''
LC 34: Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
Input: nums = [5,7,7,8,8,10], target = 8 Output: [3,4]
Input: nums = [5,7,7,8,8,10], target = 6 Output: [-1,-1]
'''
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left, right = 0, len(nums) - 1
        if not nums:
            return [-1, -1]
        
        def find_min(left, right):
            while left <= right:
                # Check if mid matches the target
                mid = (left + right) // 2
                if nums[mid] == target:
                    # Check if this is the least index of the number
                    # If mid == left, it means its the only element in this subarray
                    if mid == left or nums[mid - 1] < target:
                        return mid
                    right = mid - 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        
        def find_max(left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    # Check if this is the max index of the number
                    # If mid == right, it means its the only element in this subarray
                    if mid == right or nums[mid + 1] > target:
                        return mid
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
            
        
        return [find_min(left, right), find_max(left, right)]

find_range = Solution().searchRange
print (find_range([5,7,7,8,8,10], 8))
print (find_range([5,7,7,8,8,10], 6))
print (find_range([2,2], 3))
        