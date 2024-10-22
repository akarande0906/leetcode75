class Solution:
   def numSubArrayProductLessThanK(self, nums: list[int], k:int) -> int:
      res = 0
      product = 1
      lptr = 0
      res_arr = []
      prod_arr = []
      for rptr in range(len(nums)): 
         product = product * nums[rptr]
         while lptr <= rptr and product >= k:
            product = product / nums[lptr]
            lptr += 1
         res += rptr - lptr + 1 # This is because we also need to add the array with single element
         prod_arr = nums[lptr: rptr+1]
         while prod_arr:
            res_arr.append(prod_arr.copy())
            prod_arr.pop()
      return res_arr


print(Solution().numSubArrayProductLessThanK([10,2,4,6], 100))
  
