'''
Leetcode 54: Spiral Matrix
'''
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # To traverse in a spiral order, we need to first move column wise, then row wise
        # Keep track of all visited nodes, and finally stop when all nodes are visited.
        rows, cols = len(matrix), len(matrix[0])
        x, y, dx, dy = 0, 0, 0, 1 # We start at 0, 0 and first traverse along the first row
        spiral_result = []

        for _ in range(rows * cols): # We have to traverse all the nodes
            spiral_result.append(matrix[x][y])
            matrix[x][y] = '.' # This is to avoid traversing this cell again
            if not 0 <= x + dx  < rows or not 0 <= y + dy < cols or matrix[x+dx][y+dy] == '.':
                dx, dy = dy, -dx # For the first switch, dx will 1 and dy will be 0, then dx will be 0 and dy will be -1 and so on
            x = x + dx
            y = y + dy
        return spiral_result
    
order = Solution().spiralOrder
print(order([[1,2,3],[4,5,6],[7,8,9]]))
print(order([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(order([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))

# Time Complexity = O(M*N), Space Complexity = O(M+N), however output is not considered, so O(1)


        
