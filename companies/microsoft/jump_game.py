'''
Leetcode 55: Jump Game
'''
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Here we find if at any point if we can reach the next position
        # Can use greedy algorithm here as we go backwards to check if we can reach the starting pos
        lastPos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastPos: 
                # We see if we can jump from this position to the last position
                # If so we set this as the last position and check the previous elements
                lastPos = i
        return lastPos == 0 # If we reach the start, it means we can jump from here
    
jump = Solution().canJump
print(jump([2,3,1,1,4]))
print(jump([3,2,1,0,4]))

# Time Complexity: O(n), Space Complexity: O(1)



