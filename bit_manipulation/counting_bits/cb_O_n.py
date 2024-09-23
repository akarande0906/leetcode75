class Solution:
    def fetchOnes(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n & 1
            n = n >> 1
        return count    
    def countBits(self, n: int) -> list[int]:
        ret_arr = [0]
        m = 1
        while m <= n:
            ret_arr.append(self.fetchOnes(m))
            m += 1
        return ret_arr

sol = Solution()
print(sol.countBits(20))
print(sol.countBits(5))
