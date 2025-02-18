'''
LC 463: Island Perimeter
'''
from collections import deque

class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        start = (-1, -1)
        perimeter = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    if not visited:
                        start = (r, c)
                    visited.add((r,c))
        queue = deque()
        queue.append(start)
        visited.remove(start)
        while queue:
            row, col = queue.popleft()
            perimeter += 4
            # Get neighbors
            neighbors = [(-1,0), (0,-1), (1,0), (0,1)]
            for n in neighbors:
                n_row, n_col = row + n[0], col + n[1]
                if n_row >= 0 and n_col >= 0 and n_row < rows and n_col < cols:
                    if grid[n_row][n_col]:
                        perimeter -= 1
                    if (n_row, n_col) in visited:
                        queue.append((n_row, n_col))
                        visited.remove((n_row, n_col))
        return perimeter
# Time: O(rc)
# Space: O(rc)

# Alternative solution (O(1) space)
    def islandPerimeter_v2(self, grid: list[list[int]]) -> int:
            rows = len(grid)
            cols = len(grid[0])
            visited = set()
            perimeter = 0
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c]:
                        perimeter += 4
                        # Check neighbors
                        neighbors = [(-1,0), (0,-1)]
                        for n in neighbors:
                            n_row, n_col = r + n[0], c + n[1]
                            if n_row >= 0 and n_col >= 0 and n_row < rows \
                                and n_col < cols and grid[n_row][n_col]:
                                # We only check left and top neighbors and subtract two since 
                                # it removes one edge from current cell and neighbor
                                perimeter -= 2
            return perimeter
# Time: O(rc)
# Space: O(1)
# islandPerimeter = Solution().islandPerimeter
islandPerimeter = Solution().islandPerimeter_v2
assert islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]) == 16
assert islandPerimeter([[1]]) == 4
assert islandPerimeter([[1,0]]) == 4
assert islandPerimeter([[1,1],[1,1]]) == 8
