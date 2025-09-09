'''
Leetcode 48: Rotate Image
'''
from typing import List

class Solution:
    def printMatrix(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            row = []
            for j in range(n):
                row.append(str(matrix[i][j]))
            print(' '.join(row))
        print('')
    

    def rotate(self, matrix: List[List[int]]) -> None:
        # In place rotation
        # First we reverse and then transpose (swap rows and columns) 
        '''
        1 2 3       7 8 9       7 4 1
        4 5 6  =>   4 5 6   =>  8 5 2 
        7 8 9       1 2 3       9 6 3
        '''
        self.printMatrix(matrix)
        n = len(matrix)
        
        # Reverse matrix
        low, high = 0, n - 1
        while low < high:
            matrix[low], matrix[high] = matrix[high], matrix[low]
            low += 1
            high -= 1
        self.printMatrix(matrix)

        # Transpose the matrix now
        for row in range(n):
            for col in range(row):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        self.printMatrix(matrix)


sol = Solution()
sol.rotate([[1,2,3],[4,5,6],[7,8,9]])
sol.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])