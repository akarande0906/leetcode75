'''
LC 18: 4Sum
Given an array nums of n integers, return an array of all the unique quadruplets
'''
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        if len(nums) < 4:
            return []
        # First Sort the array
        seen = set()
        nums.sort()
        return_arr = []
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                left, right = j+1, len(nums) - 1
                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    tup = (nums[i], nums[j], nums[left], nums[right])
                    if sum == target:
                        if tup not in seen:
                            return_arr.append(list(tup))
                            seen.add(tup)
                        left += 1
                        right -= 1
                    elif sum < target:
                        left += 1
                    else:
                        right -= 1
        return return_arr
    
# Time Complexity: O(N^3) where N is the length of the array
# Space Complexity: O(N) as we are using a set to store the unique quadruplets