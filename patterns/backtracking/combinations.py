'''
LC 77: Combinations
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
Example 1: n = 4, k = 2 -> [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
'''
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        temp_arr = []
        def get_combo(temp_arr, index):
            if len(temp_arr) == k:
                result.append(temp_arr.copy())
                temp_arr = []
                return
            for j in range(index + 1, n+1):
                temp_arr.append(j)
                get_combo(temp_arr, j)
                temp_arr.pop()
        get_combo(temp_arr, 0)
        return result
    
print (Solution().combine(4, 2)) # [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
print (Solution().combine(4, 3)) # [[1,2,3],[1,2,4],[1,3,4],[2,3,4]]
print (Solution().combine(5, 2)) # [[1,2],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5],[3,4],[3,5],[4,5]]