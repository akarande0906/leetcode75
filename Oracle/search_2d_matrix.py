''' 
LC 74: Search a sorted 2D Matrix
'''
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # First do binary search on the row and then find the col where the 
        # value might lie 
        rows = len(matrix)
        cols = len(matrix[0])
        low, high = 0, rows - 1
        while low <= high: 
            mid = (low + high) // 2
            if matrix[mid][0] == target or matrix[mid][cols - 1] == target:
                return True
            if matrix[mid][0] > target:
                high = mid - 1
            elif matrix[mid][cols - 1] < target:
                low = mid + 1
            else:
                # We have found the row where target should be. Move on to phase 2
                break
        row = mid
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
# Time: O(log(m) + log(n))
# Space: O(1)
search = Solution().searchMatrix
assert search([[1,3]], 3) == True
assert search([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3) == True
assert search([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13) == False
assert search([[1,3,5,7],[9,11,13,15],[17,19,21,23]], 23) == True
assert search([[1,3,5,7],[9,11,13,15],[17,19,21,23]], 24) == False
