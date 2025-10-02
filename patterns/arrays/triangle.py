'''
LeetCode 120: Triangle
'''
from typing import List

# We start with the 2nd last row from the bottom
# For each column we find the min sum at that column by taking the min of that 
# column and column + 1 added to the value of the column
# That way as we move up, we can arrive at the min path
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        max_row = len(triangle) - 1
        below_row = triangle[-1]

        for row in range(max_row - 1, -1, -1):
            cur_row = []
            for col in range(len(triangle[row])):
                cur_row.append(min(below_row[col], below_row[col+1]) + triangle[row][col])
            below_row = cur_row
        return below_row[0] # Finally the topmost cell will have the min path
    

minPath = Solution().minimumTotal
print(minPath([[2],[3,4],[6,5,7],[4,1,8,3]]))
print(minPath([[-10]]))

# Time Complexity = O(n*m)
# Space Complexity = O(n)

