class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.columns = [0] * n
        self.diagonal = 0
        self.antidiag = 0

    def move(self, row: int, col: int, player: int) -> int:
        curPlayer = 1 if player == 1 else -1
        if row == col:
            self.diagonal += curPlayer
        if row + col == self.n - 1:
            self.antidiag += curPlayer
        self.rows[row] += curPlayer
        self.columns[col] += curPlayer
        # If a row or column or diagonal or antidiagonal reaches the count, return winning player
        if abs(self.rows[row]) == self.n or abs(self.columns[col]) == self.n or abs(self.diagonal) == self.n or abs(self.antidiag) == self.n:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
