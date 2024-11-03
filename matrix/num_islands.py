from collections import deque 

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        unvisited =  set()
        numIslands = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    tup = (row, col)	
                    unvisited.add(tup)

        while len(unvisited) > 0:
            startingCell = unvisited.pop()
            exploreLand(grid, startingCell, unvisited)

            numIslands += 1

        return numIslands


def exploreLand(grid: list[list[str]], startingCell: tuple[int, int], unvisited: set[tuple[int, int]]):
    queue: Deque[Tuple[int, int]] = deque([startingCell])
    numRows = len(grid)
    numCols = len(grid[0])

    while len(queue) > 0:
        row, col = queue.popleft()
        upCell = (row - 1, col)
        downCell = (row + 1, col)
        leftCell = (row, col - 1)
        rightCell = (row, col + 1)

        for cell in [upCell, downCell, leftCell, rightCell]:
            isValidCell = 0 <= cell[0] < numRows and 0 <= cell[1] < numCols
            if not isValidCell or cell not in unvisited:
                continue

            unvisited.remove(cell)
            queue.append(cell)


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
