'''
Given a Snakes & Ladders board, list the min number of moves to reach the final square
For example if the board is 10 X 10 , find the min moves to reach from 1 to 100 using ladders and/or snakes
'''
from collections import deque

class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        board.reverse()
        dimension = len(board)
        def getRowColumn(cell):
            row = cell // dimension
            col = cell % dimension
            if row % 2:
                col = dimension - col - 1
            return (row, col)
        
        q = deque()
        numTurns = 0
        cell = 1
        q.append((cell, numTurns))
        visited = set()
        # Use BFS to run through the decision tree
        # Avoid visiting cells already visited since we want min moves
        while q:
            cell, numTurns = q.popleft()
            for i in range (1, 7): # Roll of the dice
                newCell = cell + i 
                row, col = getRowColumn(newCell - 1)
                if board[row][col] != -1:
                    newCell = board[row][col]
                if newCell == dimension ** 2:
                    return numTurns + 1
                if not newCell in visited:
                    q.append((newCell, numTurns + 1))
                    visited.add(newCell)
        return -1


snl = Solution().snakesAndLadders
print (snl([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))
print (snl([[-1,-1],[-1,3]]))        
print (snl([[-1,-1,-1],[-1,9,8],[-1,8,9]]))

'''
   VALUES          CELLS
| -1  8  9 |  => | 1 2 3 |
| -1  9  8 |     | 6 5 4 |
| -1 -1 -1 |     | 7 8 9 |
'''