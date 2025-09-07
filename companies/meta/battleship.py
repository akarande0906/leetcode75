'''
LC 419: Battleships in a board
Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.
Battleships can only be placed horizontally or vertically on board. In other words, 
they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. 
At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).
'''
from collections import deque
class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        bs_cells = []
        visited = set()
        self.ships = 0
        rows = len(board)
        cols = len(board[0])
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'X':
                    bs_cells.append((r,c))
        if not bs_cells:
            return 0 

        def find_battleship(row, col, is_vertical):
            queue = deque()
            queue.append((row, col, is_vertical))
            found = False
            while queue:
                r, c, is_v = queue.popleft()
                visited.add((r,c))
                board[r][c] = '.'
                if is_v: 
                    neighbors = [(r-1, c), (r+1, c)]
                else:
                    neighbors = [(r, c-1), (r, c+1)]
                for r1,c1 in neighbors:
                    if r1 >= 0 and c1 >= 0 and not (r1,c1) in visited and r1 < rows and c1 < cols and board[r1][c1] == 'X':
                        found = True
                        #bs_cells.remove((r1,c1))
                        #board[r1][c1] = '.'
                        queue.append((r1,c1, is_vertical))
                    if (r1,c1) in bs_cells:
                        bs_cells.remove((r1,c1))
            return found

        while bs_cells:
            row, col = bs_cells.pop(0)
            if not find_battleship(row, col, True):
                find_battleship(row, col, False)
            self.ships += 1
        return self.ships

                
num_ships = Solution().countBattleships
print (num_ships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]))
print (num_ships([["X","X","X","X"],[".",".",".","X"],[".",".",".","X"]]))
print (num_ships([['.']]))
print (num_ships([['X','X','X'],['.','X','.'],['X','.','X']]))