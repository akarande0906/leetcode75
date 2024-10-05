class Solution:
   def find_next_large_number(self, num: int) -> int:
      c = num
      c0 = 0 # Number of 0s to the right
      c1 = 0 # Number of 1s to the right
      while c & 1 == 0 and c != 0:
         c0 += 1
         c = c >> 1
      while c & 1 == 1:
         c1 += 1
         c = c >> 1
      if c0 + c1 == 31 or c0 + c1 == 0: # Cannot have a number thats larger than this with same number of 1s
         return -1
      p = c0 + c1 # The first non-trailing zero
      # Flip the first non trailing zero
      num = num | 1 << p
      # Reset all bits to the right of p
      mask = ~((1 << p) - 1) # ~ is a complement: if p = 7 then this is complement of 127 which i -128: 10000000
      num = num & mask
      num = num | (1 << (c1 - 1)) - 1 # Insert c1 - 1 ones to the right  
      return num

sol = Solution()
print(bin(sol.find_next_large_number(0b11011001111100)))
