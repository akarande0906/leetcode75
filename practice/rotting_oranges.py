from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        total = 0
        rows = len(grid)
        cols = len(grid[0])
        rots, fresh = 0,0
        rotted = deque()
        # Find rotting oranges and put it in a set
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotted.append((i,j))
        if fresh == 0:
            return 0
        
        while rotted:
            rot_count = len(rotted)
            rot_found = False
            for r in range(rot_count):
                row, col = rotted.popleft()
                adj_cells = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]            
                for r,c in adj_cells:
                    if (
                        r >= 0 and r < rows and c >= 0 and c < cols and
                        grid[r][c] == 1
                    ):
                        fresh -= 1
                        grid[r][c] = 2
                        rotted.append((r,c))
                        rot_found = True
            if rot_found:
                total += 1    
            if fresh == 0:
                return total
        return -1


print (Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print (Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))

