'''
Leetcode 994: Rotting Oranges
'''
from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 0: empty cell, 1: fresh orange, 2: rotten orange
        time = 0
        rows, cols = len(grid), len(grid[0]) 
        fresh, rotten = 0, deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    rotten.append((row, col))
        if not fresh:
            return 0
        
        while rotten and fresh > 0:
            for _ in range(len(rotten)):
                row, col = rotten.popleft()
                # Get neighbors of this rotten fruit
                neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
                for n_row, n_col in neighbors:
                    if (
                        n_row >= 0 and n_row < rows and n_col >= 0 
                        and n_col < cols and grid[n_row][n_col] == 1
                    ):
                        grid[n_row][n_col] = 2
                        rotten.append((n_row, n_col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1

rotted = Solution().orangesRotting
print(rotted([[2,1,1],[1,1,0],[0,1,1]]))
print(rotted([[2,1,1],[0,1,1],[1,0,1]]))
print(rotted([[0,2]]))

# Time Complexity: O(m*n), Space Complexity: O(m*n)



                
