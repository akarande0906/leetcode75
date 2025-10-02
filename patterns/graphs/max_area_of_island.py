'''
Leetcode 695: Max Area of Island
'''
from typing import List
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:

        def iterate_island(row, col):
            area = 0
            queue = deque([(row, col)])
            while (queue):
                r, c = queue.popleft()
                grid[r][c] = 0
                area += 1
                nbors = [(0,-1), (0,1), (-1,0), (1,0)]
                for n in nbors:
                    n_row, n_col = r + n[0], c + n[1]
                    if not (n_row, n_col) in visited and n_row >= 0 and n_row < len(grid) and n_col >= 0 and n_col < len(grid[0]) and grid[n_row][n_col] == 1:
                        visited.add((n_row, n_col))
                        queue.append((n_row, n_col))
            return area

        visited = set()
        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    visited.add((row, col))
                    area = iterate_island(row, col)
                    max_area = max(area, max_area)
        return max_area
    
islands = Solution().maxAreaOfIsland
print (islands([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))

# Time complexity: O(M*N) as we iterate over all elements. The visited ensures that we dont revisit nodes already visited
# Space complexity: O(M*N) for the visited set. Even though it will not have all elements it could have (M/2 * N/2) if we have alternating 1s
