'''
LC 1091: Shortest Path in Binary Matrix
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.
A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.
'''
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if grid[0][0]:
            return -1
        m = len(grid)
        n = len(grid[0])
        visited = set()
        queue = deque()
        queue.append((0,0,1))
        while queue:
            row, col, level = queue.popleft()
            if row == m-1 and col == n-1:
                return level
            neighbors = [(row-1,col), (row+1,col), (row,col-1), (row,col+1), (row-1,col-1), (row-1,col+1), (row+1,col-1), (row+1,col+1)]
            for r,c in neighbors:
                if r >= 0 and c >= 0 and r < m and c < n and grid[r][c] == 0 and not (r,c) in visited:
                    queue.append((r, c, level+1))
                    visited.add((r,c))
        return -1

shortestPath = Solution().shortestPathBinaryMatrix
grid = [[1,0,0],[1,1,0],[1,1,0]]
print (shortestPath(grid))
grid = [[0,0,0],[1,1,0],[1,1,0]]
print (shortestPath(grid))
grid = [[0,1],[1,0]]
print (shortestPath(grid))
            