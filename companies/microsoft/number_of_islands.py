'''
Leetcode 200: Number of Islands
'''
from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def visit_node(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == '0':
                return
            grid[row][col] = '0'
            neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for n in neighbors:
                visit_node(row + n[0], col + n[1])
        
        num_islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    visit_node(row, col)
                    num_islands += 1
        return num_islands
    
    def numIslands_BFS(self, grid: List[List[str]]) -> int:
        num_islands = 0

        def visit_node(row, col):
            queue = deque([(row, col)])
            while queue:
                row, col = queue.popleft()
                if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) and grid[row][col] == '1':
                    # Get neighbors and add to the queue
                    grid[row][col] = '0'
                    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    for n in neighbors:
                        queue.append((row + n[0], col + n[1]))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    visit_node(row, col)
                    num_islands += 1
        return num_islands
        

islands = Solution().numIslands
print (islands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
print (islands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))

islands = Solution().numIslands_BFS
print (islands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
print (islands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))