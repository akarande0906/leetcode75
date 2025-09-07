'''
LC 529: Minesweeper
'''

class Solution:
    def updateBoard(self, board: list[list[str]], click: list[int]) -> list[list[str]]:
        visited = set()
        m = len(board)
        n = len(board[0])
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        def dfs(row, col):           
            neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1), (row-1,col-1),(row+1,col-1),(row-1,col+1),(row+1,col+1)]
            mines = 0
            for r, c in neighbors:
                if r >=0 and c >= 0 and r < m and c < n and board[r][c] == 'M':
                    mines += 1
            if mines:
                board[row][col] = str(mines)
            else:
                board[row][col] = 'B'
                for r,c in neighbors:
                    if r >= 0 and c >= 0 and r < m and c < n and (r, c) not in visited and board[r][c] == 'E':
                        dfs(r, c)
                        visited.add((r,c))
        dfs(click[0], click[1])
        return board
    def print_board(self, board):
        for row in board:
            print (' '.join(row))
        print ('')
sol = Solution()
board = sol.updateBoard([["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], [3,0])
sol.print_board(board)
board = sol.updateBoard([["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], [1,2])
sol.print_board(board)



        