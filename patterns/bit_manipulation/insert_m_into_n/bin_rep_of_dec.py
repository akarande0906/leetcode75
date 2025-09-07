class Solution:
   def convert_to_binary(self, num : int) -> int:
      if num < 0 or num > 1:
         return "ERROR"
      bin_rep = ''
      while num > 0:
         if len(bin_rep) > 32:
            return bin_rep
         r = 2 * num
         if r >= 1:
            bin_rep += '1'
            num = r - 1
         else:  
            bin_rep += '0'
            num = r
      return bin_rep


sol = Solution()
print(sol.convert_to_binary(0.75))
print(sol.convert_to_binary(0.77))
