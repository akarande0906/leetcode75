'''
LC 162: Find Peak Element
A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
You must write an algorithm that runs in O(log n) time.
'''
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        # Use binary search to find the local maximum and
        # see if you can find if it meets the criteria
        def binary_search(left, right):
            if left == right:
                return left
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                return binary_search(left, mid)
            else:
                return binary_search(mid+1, right)
        return binary_search(0, len(nums) - 1)
    
    def findPeakElementIterative(self, nums: list[int]) -> int:
        # Use binary search to find the local maximum and
        # see if you can find if it meets the criteria
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left
    

print(Solution().findPeakElement([1,2,3,1]))
print(Solution().findPeakElementIterative([1,2,1,3,5,6,4]))
print(Solution().findPeakElementIterative([1,2,3,4,5,6,7,8]))
print(Solution().findPeakElementIterative([9,8,7,6,5,4,3,2,1]))
print(Solution().findPeakElementIterative([10,9,8,11,7,8,10,12,14,15,16]))


                
    