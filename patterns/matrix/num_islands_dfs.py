def numIslands(grid):
    islands = 0

    def explore(r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
             return False
        if grid[r][c] == '0':
            return False
        grid[r][c] = '0'
        explore(r-1, c)
        explore(r+1, c)
        explore(r, c+1)
        explore(r, c-1)
  
        return True

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1':
               explore(r,c)
               islands += 1
    return islands


print(numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
print(numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
    

'''
1 1 1 1 0
1 1 0 1 0
1 1 0 0 0
0 0 0 0 0

1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
'''     
    
