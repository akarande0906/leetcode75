'''
LC 120: Triangle
'''
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        min_sum = float('inf')
        max_row = len(triangle) - 1
        dp = {}
            
        for row in range(max_row, -1, -1):
            for col in range(len(triangle[row])):
                if row == max_row:
                    dp[(row, col)] = triangle[row][col]
                else:
                    dp[(row,col)] = min(dp[(row+1, col)] + triangle[row][col]
                        , dp[(row+1,col+1)] + triangle[row][col])
        return dp[(0,0)]
    # Time Complexity: O(n^2) where n is the number of elements in the triangle
    # Space Complexity: O(n^2) to maintain the dp array - Can be optimized to O(n) by using a 1D array
    
    def minimumTotal_optimal_space(self, triangle: list[list[int]]) -> int:
        min_sum = float('inf')
        max_row = len(triangle) - 1
        below_row = triangle[-1]
            
        for row in range(max_row - 1, -1, -1):
            cur_row = []
            for col in range(len(triangle[row])):
                cur_row.append(min(below_row[col], below_row[col+1]) + \
                    triangle[row][col])
            below_row = cur_row
        return below_row[0]
    # Time Complexity: O(n^2) where n is the number of elements in the triangle
    # Space Complexity: O(n) to maintain the 1d arrays


minimumTotal = Solution().minimumTotal
print(minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
print(minimumTotal([[-10]]))
print(minimumTotal([[-1],[2,3],[1,-1,-3]]))
