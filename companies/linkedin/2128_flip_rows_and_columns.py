class Solution:
    def removeOnes(self, grid: list[list[int]]) -> bool:
        m = len(grid)  # get dimensions of grid
        n = len(grid[0])
        for i in range(n):  # flip columns so that first row only has 0's
             if grid[0][i] == 1:
                 for j in range(m):  # flips a column
                     grid[j][i] = 1 - grid[j][i]
        ans = True
        for i in range(m):  # checks if each row has all 0's or all 1's
             sum = 0
             for j in range(n):
                 sum += grid[i][j]
             if sum == 0 or sum == n:
                 continue
             ans = False
        return ans

print(Solution().removeOnes([[0,1,0],[1,0,1],[0,1,0]]))
print(Solution().removeOnes([[1,1,0],[0,0,0],[0,0,0]]))
