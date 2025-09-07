'''
2D Spiral Array
n = 3
1 2 3
8 9 4
7 6 5

n = 4
01 02 03 04
12 13 14 05
11 16 15 06
10 09 08 07
'''
def create2DSpiralArray(num):
    if not num:
        return None
    if num == 1:
        return [[1]]
    else:
        matrix = [[0] * num for _ in range(num)]
        x, y, dx, dy = 0, 0, 1, 0
        val = 0
        while val < num * num:
            val += 1
            matrix[y][x] = val
            x += dx
            y += dy
            if x + dx >= num or y + dy >= num or matrix[y+dy][x+dx] != 0:
                dx, dy = -dy, dx
    return matrix

print (create2DSpiralArray(8))        


        
