from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        for i in range (1, amount + 1):
            for coin in coins:
                if coin <= i: # If coin size is > than i the coin can be skipped
                    # This computes compares the previous value for dp[i] to see if it was smaller
                    # The 1 + dp[i-coin] is adding one coin to the dp of the amount from the remaining amount after removing coin
                    dp[i] = min(dp[i], dp[i-coin] + 1)
            # print (dp)
        return dp[-1] if dp[-1] is not float('inf') else -1
        '''
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]
        '''

    def coinChangeMemo(self, coins: List[int], amount: int) -> int:
        memo = {0:0}
        def coinChangeHelper(currentSum):
            answer = float('inf')
            if currentSum in memo:
                return memo[currentSum]
            if currentSum == 0:
                answer = 0
            else:
                for coin in coins:
                    if currentSum - coin < 0:
                        continue
                    # We add 1 for this coin
                    answer = min(answer, coinChangeHelper(currentSum - coin) + 1)
            memo[currentSum] = answer 
            return answer
        return coinChangeHelper(amount)
                
        
'''
print(Solution().coinChange([1,2,5], 11))
print(Solution().coinChange([1,2,5], 5))
print(Solution().coinChange([1,7,9], 21))
'''
print(Solution().coinChangeMemo([1,2,5], 11))
print(Solution().coinChangeMemo([1,2,5], 5))
print(Solution().coinChangeMemo([1,7,9], 21))

