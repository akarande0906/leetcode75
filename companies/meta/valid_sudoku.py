'''
LC 36: Valid Sudoku
Determine if a 9x9 Sudoku board is valid. 
Only the filled cells need to be validated. 
Return true if the Sudoku board is valid, otherwise return false.
'''
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # We need to construct three paths to validate uniqueness: Row, Column, 3X3 grid
        # If we dont find duplicates across all three, we indicate this is valid.
        # If duplicates are found, return False immediately
        rows = [set() for _ in range(9)] # We have a total of 9 rows
        cols = [set() for _ in range(9)] # We have a total of 9 columns
        grids = [set() for _ in range(9)] # We have a total of 9 grids

        # Iterate of each cell and check if the value at that cell is present 
        # in its corresponding row, column and grid. If not, add it to these sets
        # and continue, else return False
        for row in range(0, len(board)):
            for col in range(0, len(board[0])):
                if board[row][col] == '.':
                    continue
                num = board[row][col]
                grid = 3 * (row // 3) + col // 3
                if num in rows[row] or num in cols[col] or num in grids[grid]:
                    return False
                rows[row].add(num)
                cols[col].add(num)
                grids[grid].add(num)
        return True

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print (Solution().isValidSudoku(board)) # True
board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".","8",".",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print (Solution().isValidSudoku(board)) # False

# Time Complexity: O(1) since we are iterating over a fixed 9X9 board
# Space Complexity: O(1) since we are using fixed size sets for rows, columns and grids
