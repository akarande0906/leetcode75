from collections import deque 
''' LC: 200 '''
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        unvisited =  set()
        numIslands = 0

        def bfs(row, col):
            queue = deque()
            queue.append([row, col])
            while len(queue) > 0:
                row, col = queue.popleft()
                upCell = (row - 1, col)
                downCell = (row + 1, col)
                leftCell = (row, col - 1)
                rightCell = (row, col + 1)

                for cell in [upCell, downCell, leftCell, rightCell]:
                    if (
                        cell[0] < 0 or cell[1] < 0 or 
                        cell[0] >= len(grid) or cell[1] >= len(grid[0]) or
                        grid[cell[0]][cell[1]] == '0'
                    ):
                        continue
                    grid[cell[0]][cell[1]] = '0'
                    queue.append([cell[0], cell[1]])

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    bfs(row, col)
                    numIslands += 1
        return numIslands


print(Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
print(Solution().numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))

'''
1 1 1 1 0
1 1 0 1 0
1 1 0 0 0
0 0 0 0 0

1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
'''
