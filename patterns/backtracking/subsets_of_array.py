from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []
        ret = []
        n = len(nums)

        def backtrack(i=0):
            if i == n:
                ret.append(sol[:])
                return
            backtrack(i+1)
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        backtrack()
        return ret


print(Solution().subsets([1,2,3]))
