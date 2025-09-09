'''
Leetcode 15: 3 Sum
'''
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        output_array = []
        for i in range(n):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right] 
                if total == 0:
                    output_array.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    if left < right and nums[left] == nums[left - 1]:
                        left += 1
                    if left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0: # Then we need to move right
                    left += 1
                    if left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
                    if left < right and nums[right] == nums[right + 1]:
                        left += 1
        return output_array
    
tsum = Solution().threeSum
print (tsum([-1,0,1,2,-1,-4])) # Sorted: [-4, -1, -1, 0, 1, 2]
print (tsum([0,1,1]))

        