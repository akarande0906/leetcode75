'''
LC 746: Min Cost Climbing Stairs
'''
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        step_count = len(cost)
        if step_count == 2:
            return min(cost[0], cost[1])
        dp = [0] * (step_count + 1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, step_count):
            if i < step_count:
                dp[i] = min(dp[i-2], dp[i-1]) + cost[i]
        dp[step_count] = min(dp[step_count - 1], dp[step_count - 2])
        return dp[step_count]

    # TC : O(N)
    # SC : O(N)
    
    def minCostClimbingStairs_v2(self, cost: list[int]) -> int:
        step_count = len(cost)
        if step_count == 2:
            return min(cost[0], cost[1])
        # We can use two variables here instead of using an array as we will only need the last two values
        first = cost[0]
        second = cost[1]

        for i in range(2, step_count):
            if i < step_count:
                first, second = second, min(first, second) + cost[i]
        return min(first, second)
    
    # TC : O(N)
    # SC : O(1)
    
minCost = Solution().minCostClimbingStairs
print(minCost([10, 15, 20]))
print(minCost([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
print(minCost([0, 0, 0, 0]))
print(minCost([1, 1, 1, 1]))
