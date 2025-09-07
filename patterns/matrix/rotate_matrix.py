'''
48. Rotate Image
'''
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        #Reverse rows
        l = 0
        r = n - 1
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1
        # Transpose matrix
        for y in range(n):
            for x in range(y, n):
                matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]
        print (matrix)

        # TC: O(n*n)
        # SC: O(1)


Solution().rotate([[1,2,3],[4,5,6],[7,8,9]])
Solution().rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
