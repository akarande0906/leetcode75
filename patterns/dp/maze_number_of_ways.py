'''
Consider an mxn maze where a rabbit starts at the top left corner and can only move either right on down. 
Count the number of ways it can get to the bottom right of the maze
--------------------
| x|  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  | y|
--------------------
'''
def grid_paths(m, n):
    
    memo = {}
    # First get set the base cases
    # Here to get to the first column of every row or the first row of every column
    # there is only one way to get there 
    for i in range(1, m+1):
        memo[(i, 1)] = 1
    for j in range(1, n+1):
        memo[(1, j)] = 1
    # To get to any cell we can either come from the left or the top
    # So we need to add those two
    for i in range(2, m+1):
        for j in range(2, n+1):
            memo[(i,j)] = memo[(i-1, j)] + memo[(i, j-1)]
    return memo[(m,n)]

print (grid_paths(2, 2))
print (grid_paths(18, 6))
print (grid_paths(75, 19))