'''
LC 16: 3Sum Closest
Given an integer array nums of length n and an integer target, 
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
'''
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # Sort the array
        nums.sort()
        min_sum = float('inf')
        min_diff = float('inf')
        for n in range(len(nums)):
            left, right = n + 1, len(nums) - 1
            while left < right:
                sum = nums[n] + nums[left] + nums[right]
                diff = abs(sum - target)
                if diff < min_diff:
                    min_sum = sum
                    min_diff = diff
                if sum < target:
                    left += 1
                else:
                    right -= 1
        return min_sum

# Time Complexity: O(N^2) where N is the length of the array
# Space Complexity: O(1) as we are not using any extra space (Sort uses O(log N) space however)

threeSum = Solution().threeSumClosest
print(threeSum([-1,2,1,-4], 1))
print(threeSum([0,0,0], 1))
print(threeSum([1,1,1,0], -100))