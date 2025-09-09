'''
Leetcode 198: House Robber
'''
from typing import List

class Solution:
    def rob(self, houses: List[int]) -> int:
        if len(houses) == 1:
            return houses[0]
        # Either the robber can steal from the first or the 2nd house based on which is greater
        houses[1] = max(houses[0], houses[1])
        for h_index in range(2, len(houses)):
            # At any house, the robber can decide to steal from the previous house or
            # from two houses before plus this house. He always chooses the greater value
            houses[h_index] = max(houses[h_index] + houses[h_index - 2], houses[h_index - 1])
        return houses[-1]
    
rob = Solution().rob
print (rob([1,2,3,1]))
print (rob([2,7,9,3,1]))