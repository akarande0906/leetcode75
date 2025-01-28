'''
LC 329: Longest increasing path in a matrix
'''
class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        cache = [[0 for _ in range(cols)] for _ in range(rows)]
        max_path_length = 0

        def is_valid(row, col, r_new, c_new):
            if r_new < rows and c_new < cols and r_new >= 0 and c_new >= 0 and \
                matrix[row][col] < matrix[r_new][c_new]:
                return True
            return False
        def iterateIncreasingPath(row, col):
            if not cache[row][col]:
                max_path_len = 0
                for d in directions:
                    if is_valid(row, col, row + d[0], col + d[1]):
                        max_path_len = \
                            max(max_path_len, iterateIncreasingPath(row + d[0], col + d[1]))
                cache[row][col] = max_path_len + 1             
            return cache[row][col]
        
        for r in range(rows):
            for c in range(cols):
                max_path_length = max(max_path_length, iterateIncreasingPath(r,c))
        return max_path_length

# Time Complexity = O(row*cols)
# Space Complexity = O(row*cols)

long_path = Solution().longestIncreasingPath
print(long_path([[9,9,4],[6,6,8],[2,1,1]]))
print(long_path([[3,4,5],[3,2,6],[2,2,1]]))
print(long_path([[1]]))
      