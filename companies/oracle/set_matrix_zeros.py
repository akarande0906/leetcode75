'''
LC 73: Set Matrix Zeros
'''
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # We can find all 0s mark the neighbors as float('inf')
        # Then we can iterate over the matrix again and mark 
        # all such instances to 0
        def mark_neighbors(row, col):
            for r in range(rows):
                if matrix[r][col] != 0:
                    matrix[r][col] = float('inf')
            for c in range(cols):
                if matrix[row][c] != 0:
                    matrix[row][c] = float('inf')
            
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    mark_neighbors(r, c)
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == float('inf'):
                    matrix[r][c] = 0
        print (matrix)
# Time: O(m * n)
# Space: O(1)
set_zeros = Solution().setZeroes

set_zeros([[1,1,1],[1,0,1],[1,1,1]]) # Expected [[1,0,1],[0,0,0],[1,0,1]]
set_zeros([[0,1,2,0],[3,4,5,2],[1,3,1,5]]) # Expected [[0,0,0,0],[0,4,5,0],[0,3,1,0]]   
                
        