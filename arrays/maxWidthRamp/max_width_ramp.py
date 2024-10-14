'''Leetcode 962 '''
class Solution:
   def maxWidthRamp(self, nums: list[int]) -> int:
      # First find the max value at the right and add it to an array
      max_val = 0
      max_array = [0] * len(nums) 
      for i in range(len(nums) - 1, -1, -1): # creates a reverse iterator
          max_val = max(max_val, nums[i])
          max_array[i] = max_val
      print (max_array)
      lptr = 0
      ramp_len = 0
      for rptr in range(len(nums)):
          while nums[lptr] > max_array[rptr]:
             lptr += 1
          ramp_len = max(ramp_len, rptr - lptr)       
      return ramp_len

print(Solution().maxWidthRamp([6,0,8,2,1,5]))
print(Solution().maxWidthRamp([6,0,8,2,1,6]))
print(Solution().maxWidthRamp([2,0,1,3,2,1]))
