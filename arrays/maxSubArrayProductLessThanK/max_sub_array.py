class Solution:
   def numSubArrayProductLessThanK(self, nums: list[int], k:int) -> int:
      res = 0
      product = 1
      lptr = 0
      for rptr in range(len(nums)): 
         product = product * nums[rptr]
         while lptr <= rptr and product >= k:
            product = product / nums[lptr]
            lptr += 1
         res += rptr - lptr + 1 # This is because we also need to add the array with single element
      return res


print(Solution().numSubArrayProductLessThanK([10,2,4,6], 100))
  
