'''
Leetcode 39: Combination Sum
'''
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output_array = []

        def backtrack(idx, cur_sum, cur_arr):
            if cur_sum > target:
                return
            elif cur_sum == target:
                output_array.append(cur_arr[:])
                return 
            else:
                for i in range(idx, len(candidates)):
                    new_sum = candidates[i] + cur_sum
                    cur_arr.append(candidates[i])
                    backtrack(i, new_sum, cur_arr)
                    cur_arr.pop()

        backtrack(0, 0, [])
        return output_array

summer = Solution().combinationSum
print(summer([2,3,6,7], 7))
print(summer([2,3,5], 8))
print(summer([2], 1))
