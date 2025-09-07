'''
LC 240: Search a 2D Matrix II
'''
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            # Check if the target value is in between the min and max
            # vals in that row
            if matrix[row][0] == target or matrix[row][cols - 1] == target:
                return True
            if matrix[row][0] > target or matrix[row][cols - 1] < target: 
                # If the row doesn't contain the target, go to the next row
                continue
            else: # We can search within the row
                # Now we iterate over the columns of the selected row
                low, high = 0, cols - 1
                while low <= high:
                    mid = (low + high) // 2
                    if matrix[row][mid] == target:
                        return True
                    elif matrix[row][mid] > target:
                        high = mid - 1
                    elif matrix[row][mid] < target:
                        low = mid + 1
        return False
    # Time: O(m * log(n))
    # Space: O(1)
search = Solution().searchMatrix
assert search([[1,3]], 3) == True
assert search([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3) == True
assert search([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5) == True
assert search([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20) == False
