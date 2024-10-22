class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        for i in range (1, amount + 1):
            for coin in coins:
                if coin <= i: # If coin size is > than i the coin can be skipped
                    # This computes compares the previous value for dp[i] to see if it was smaller
                    # The 1 + dp[i-coin] is adding one coin to the dp of the amount from the remaining amount after removing coin
                    dp[i] = min(dp[i], dp[i-coin] + 1)
            print (dp)
        return dp[-1] if dp[-1] is not float('inf') else -1
        '''
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]
        '''

print(Solution().coinChange([1,2,5], 11))
print(Solution().coinChange([1,2,5], 5))
print(Solution().coinChange([1,7,9], 21))

