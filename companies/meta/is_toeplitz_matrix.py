'''
LC 766: Toeplitz Matrix
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
Input: matrix =  [[1,2,3,4],
                  [5,1,2,3],
                  [9,5,1,2]]   Output: true
Input: matrix = [[1,2],
                 [2,2]] Output: false
'''
class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] != matrix[r-1][c-1]:
                    return False
        return True

print (Solution().isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
print (Solution().isToeplitzMatrix([[1,2],[2,2]]))