'''
Leetcode 200: Number of Islands
'''
from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def iterate_island(row, col):
            queue = deque([(row, col)])
            while (queue):
                r, c = queue.popleft()
                grid[r][c] = '0'
                nbors = [(0,-1), (0,1), (-1,0), (1,0)]
                for n in nbors:
                    n_row, n_col = r + n[0], c + n[1]
                    if not (n_row, n_col) in visited and n_row >= 0 and n_row < len(grid) and n_col >= 0 and n_col < len(grid[0]) and grid[n_row][n_col] == '1':
                        visited.add((n_row, n_col))
                        queue.append((n_row, n_col))

        islands = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    visited.add((row, col))
                    iterate_island(row, col)
                    islands += 1
        return islands
    
islands = Solution().numIslands

print(islands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))

print(islands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))

print(islands([["1","0","1","0","1"],["0","1","0","1","0"],["1","0","1","0","1"],["0","1","0","1","0"]]))

# Time complexity: O(M*N) as we iterate over all elements. The visited ensures that we dont revisit nodes already visited
# Space complexity: O(M*N) for the visited set. Even though it will not have all elements it could have (M/2 * N/2) if we have alternating 1s

