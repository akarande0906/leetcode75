'''
LC 39: Combination Sum
'''
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        output_array = []
        def backtrack(idx, cur_sum, cur_arr):
            if cur_sum > target:
                return False
            if cur_sum == target:
                output_array.append(cur_arr[:])
                return False
            for i in range(idx, len(candidates)):
                new_sum = candidates[i] + cur_sum
                cur_arr.append(candidates[i])
                ret_val = backtrack(i, new_sum, cur_arr)
                cur_arr.pop()
                #if not ret_val:
                #    break
            return True
        
        #candidates.sort()
        #for i in range(len(candidates)):
        #    backtrack(i, candidates[i], [candidates[i]])
        backtrack(0, 0, [])
        return output_array
# Time Complexity: O(2^n) where n is the number of elements in the candidates array
# Space Complexity: O(n) to maintain the output array

combinationSum = Solution().combinationSum
print(combinationSum([2,3,6,7], 7))
print(combinationSum([2,3,5], 8))
print(combinationSum([2], 1))
print(combinationSum([1], 1))