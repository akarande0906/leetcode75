class Solution:  
    def countBits(self, n: int) -> list[int]:
        ret_arr = [0] * (n + 1)
        for i in range (1, n+1):
            if i % 2 == 1: # Odd numbers
                ret_arr[i] = ret_arr[i-1] + 1
            else:
                ret_arr[i] = ret_arr[i//2]
        return ret_arr

sol = Solution()
print(sol.countBits(20))
print(sol.countBits(5))
