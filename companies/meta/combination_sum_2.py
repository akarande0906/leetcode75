'''
LC 40: Combination Sum II
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.
Example: candidates = [10,1,2,7,6,1,5], target = 8 -> [[1,1,6],[1,2,5],[1,7],[2,6]]
'''
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        temp_arr = []
        n = len(candidates)
        candidates.sort()
        def backtrack(temp_arr, id, sum_left):
            if sum_left == 0:
                result.append(temp_arr.copy())
                temp_arr = []
                return
            if sum_left > 0:
                for j in range(id, n):
                    if j > id and candidates[j] == candidates[j-1]:
                        # Avoid duplicate values in combinations
                        continue
                    temp_arr.append(candidates[j])
                    backtrack(temp_arr, j+1, sum_left - candidates[j])
                    temp_arr.pop()
        backtrack(temp_arr, 0, target)
        return result
finder = Solution().combinationSum2
print (finder([10,1,2,7,6,1,5], 8)) # [[1,1,6],[1,2,5],[1,7],[2,6]]
print (finder([2,5,2,1,2], 5)) # [[1,2,2],[5]]

# Time Complexity: O(2^N) where N is the number of elements in the candidates array
# Space Complexity: O(N) where N is the number of elements in the candidates array