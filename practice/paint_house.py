'''
LC: 256: Paint House
'''

class Solution:
    def minCost(self, costs: list[list[int]]) -> int:
        dp = [0, 0, 0] # dp array for each house
        for i in range(len(costs)):
            dp0 = costs[i][0] + min(dp[1], dp[2])
            dp1 = costs[i][1] + min(dp[0], dp[2])
            dp2 = costs[i][2] + min(dp[0], dp[1])
            dp = [dp0, dp1, dp2]
        return min(dp)

print (Solution().minCost([[17,2,17],[16,16,5],[14,3,19]]))
print (Solution().minCost([[7,8,9],[6,5,4],[8,6,7]]))
print (Solution().minCost([[7,6,2]]))

'''
     17            2             17
    /  \          / \           /  \
  16    5       16   5         16   16
 / \   / \      /\    /\      / \   / \
14  3  14 3   19  3  3 14    3  19  14 19
'''
