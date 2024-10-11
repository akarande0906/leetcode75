class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        for i in range (1, amount + 1):
            for coin in coins:
                if coin <= i: # If coin size is > than i the coin can be skipped
                    dp[i] = min(dp[i], dp[i-coin] + 1)
            print (dp)
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]

print(Solution().coinChange([1,2,5], 11))
print(Solution().coinChange([1,7,9], 21))

