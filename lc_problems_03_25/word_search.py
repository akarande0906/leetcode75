'''
LC 75: Word Search
'''
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        starting_nodes = []
        word_len = len(word)
        visited = set()
        rows = len(board)
        cols = len(board[0])

        def next_word(row, col, idx):
            nonlocal rows, cols
            idx += 1
            if idx == word_len:
                return True
            nbrs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            for n in nbrs:
                n_row, n_col = row + n[0], col + n[1]
                if n_row >= 0 and n_row < rows and n_col >= 0 and n_col < cols \
                    and (n_row, n_col) not in visited:
                    if board[n_row][n_col] == word[idx]:
                        visited.add((n_row, n_col))
                        if next_word(n_row, n_col, idx):
                            return True
                        visited.remove((n_row, n_col))
            return False

        for row in range(rows):
            for col in range(cols):
                if  board[row][col] == word[0]:
                    starting_nodes.append((row, col))  

        for s in starting_nodes:
            row, col = s
            visited = set()
            visited.add((row, col))
            if next_word(row, col, 0):
                return True
        return False
            
# TC : O(m*3^l) where m is the number of rows, n is the number of columns and l is the length of the word
# SC : O(l) where l is the length of the word

exist = Solution().exist
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
print(exist([[["A", "A"]], ["A"]], "AAA"))
print(exist([["A"]], "A"))
print(exist([[["a","b"],["c","d"]]], "acbd"))
print(exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))

