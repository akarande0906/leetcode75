'''
Leetcode 73: Set Matrix Zeroes
'''
from typing import List

class Solution: 
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        def mark_neighbors(row, col):
            # Here we mark the neighbors with a marker value that we can find later. 
            # Setting the values to zero will mean all values will eventually become 0
            for r in range(rows):
                if matrix[r][col] != 0:
                    matrix[r][col] = float('inf') 
            for c in range(cols):
                if matrix[row][c] != 0:
                    matrix[row][c] = float('inf')

        # Mark all rows and cols of elements that are 0 with inf   
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    mark_neighbors(r, c)

        # Now find all elems that were marked as inf, and change them to 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == float('inf'):
                    matrix[r][c] = 0
        print (matrix)

setZ = Solution().setZeroes
setZ([[1,1,1],[1,0,1],[1,1,1]])
setZ([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
