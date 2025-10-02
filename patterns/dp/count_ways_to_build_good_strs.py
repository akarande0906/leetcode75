'''
LC 2466: Count Ways to Build Good Strings
'''
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10 ** 9 + 7
        dp = {}

        # Memoization
        def dfs(length):
            if length > high:
                return 0
            if length in dp:
                return dp[length] % mod
            dp[length] = 1 if length >= low else 0
            dp[length] += dfs(length + zero) + dfs(length + one)
            return dp[length] % mod
        
        return dfs(0)
    
    def countGoodStrings_v2(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10 ** 9 + 7
        dp = {0:1} # Base Value to start with

        # Tabulation
        for length in range(1, high + 1):
            dp[length] = dp.get(length - zero,0) + dp.get(length - one, 0)
        return sum((dp[i] for i in range(low, high + 1))) % mod

            
    
    # Time Complexity: O(n) because of memoization
    # Space Complexity: O(n) to maintain dp array
countGoodStrings = Solution().countGoodStrings_v2
print(countGoodStrings(1, 1, 1, 1))
print(countGoodStrings(2,3,1,2))
print(countGoodStrings(7, 50, 0, 0))

