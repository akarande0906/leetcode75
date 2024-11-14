'''
LC: 417
'''
class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        # All column 0 and row 0 elements can dump water to the Pacific Ocean
        # All row N and column M elements can dump water to the Atlantic Ocean
        # The goal is to do dfs on all these elements and find adjacent rows
        # that can transfer water to the source cell.

        pacific, atlantic = set(), set()
        max_rows = len(heights)
        max_cols = len(heights[0])

        def dfs(row, col, prevHeight, visited_set):
            if ( # If already visited or out of bounds
                row < 0 or row >= max_rows or col < 0 or col >= max_cols
                or (row, col) in visited_set or
                heights[row][col] < prevHeight
            ):
                return
            # If the cell satisfied the condition then add it to the set
            visited_set.add((row, col))
            neighbour_cells = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
            for n_row, n_col in neighbour_cells:
                dfs(n_row, n_col, heights[row][col], visited_set)
        overlap_array = []

        for row in range(max_rows):
            dfs(row, 0, heights[row][0], pacific)
            dfs(row, max_cols - 1, heights[row][max_cols - 1], atlantic)
        for col in range(max_cols):
            dfs(0, col, heights[0][col], pacific)
            dfs(max_rows - 1, col, heights[max_rows - 1][col], atlantic)

        for row in range(max_rows):
            for col in range(max_cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    overlap_array.append([row, col])
        return overlap_array


print (Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
