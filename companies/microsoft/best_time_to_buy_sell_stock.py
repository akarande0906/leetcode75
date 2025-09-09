'''
Leetcode 121: Best Time to Buy and Sell Stock
'''
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for sell in prices[1:]:
            if buy > sell:
                # Update the buy to this value
                buy = sell
            elif sell > buy:
                # Calculate profit
                profit = max(profit, sell - buy)
        return profit

profit = Solution().maxProfit
print (profit([7,1,5,3,6,4]))
print (profit([7,6,4,3,1]))