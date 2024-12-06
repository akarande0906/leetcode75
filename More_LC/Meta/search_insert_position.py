'''
35 Search Insert Position
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
Example 1: Input: nums = [1,3,5,6], target = 5 Output: 2
Example 2: Input: nums = [1,3,5,6], target = 2 Output: 1
Example 3: Input: nums = [1,3,5,6], target = 7 Output: 4
'''
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right and right < len(nums):
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left

search = Solution().searchInsert
arr = [1,3,5,6]
print (search(arr, 2))
print (search(arr, 5))
print (search(arr, 7))