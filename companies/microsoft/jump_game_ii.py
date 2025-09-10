'''
Leetcode 45: Jump Game II
'''
from typing import List


class Solution:
    # We use checkpoints to mark an end point for a jump
    # While we reach that jump we find the furthest we can 
    # reach by any of the nodes till the current checkpoint.
    # When we reach a checkpoint, we mwark the next checkpoint to the furthest node we calculated.
    def jump(self, nums: List[int]) -> int:
         # The starting range of the first jump is [0, 0]
        answer, n = 0, len(nums)
        cur_end, cur_far = 0, 0

        for i in range(n - 1):
            # Update the farthest reachable index of this jump.
            cur_far = max(cur_far, i + nums[i])

            # If we finish the starting range of this jump,
            # Move on to the starting range of the next jump.
            if i == cur_end:
                answer += 1
                cur_end = cur_far

        return answer

jump = Solution().jump
print(jump([2,3,1,1,4]))
print(jump([2,3,0,1,4]))
print(jump([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]))
    