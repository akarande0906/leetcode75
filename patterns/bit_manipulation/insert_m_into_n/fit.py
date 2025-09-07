class Solution:
   def insert_binary(self, n: int, m: int, i: int, j: int) -> int:
      # First create a mask of all 1s assuming 32 bit int
      mask = 2**(32-j-1) - 1
      mask = mask << (j+1)
      mask = mask | ((1 << i) - 1)
      n_cleared = n & mask
      o = n_cleared | m << i
      return o


sol = Solution()
print (bin(sol.insert_binary(0b10000000000, 0b10011, 3, 7)))
	
        
