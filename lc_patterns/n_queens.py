class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        board = [['.'] * n for _ in range(n)]
        col = set()
        posDiag = set()
        negDiag = set()
        res = []

        def findSolution(r):
            if r == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return 

            for c in range(n):
                if c in col or r+c in posDiag or r-c in negDiag:
                    continue # This is not a valid position
                
                # Assume this is a valid position
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                
                board[r][c] = 'Q'
                print ('row: ' + str(r) + ', column: ' + str(c) + ' : ' + board[r][c])
                findSolution(r+1)
                #Backtrack
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = '.'

        findSolution(0)
        return res

print (Solution().solveNQueens(4))



