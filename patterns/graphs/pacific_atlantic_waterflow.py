'''
Leetcode 417: Pacific Atlantic Water Flow
'''
# All column 0 and row 0 elements can dump water to the Pacific Ocean
# All row N and column M elements can dump water to the Atlantic Ocean
# The goal is to do dfs on all these elements and find adjacent rows
# that can transfer water to the source cell. 
# We start from the oceans and go backwards towards the buildings 
# and we track buildings we can reach. Finally we see which cells overlap 
# for the Pacific and Atlantic flow
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        max_rows, max_cols = len(heights), len(heights[0])

        def dfs(row, col, prev_height, visited):
            if (row < 0 or col < 0 or row >= max_rows or col >= max_cols 
                or (row, col) in visited or heights[row][col] < prev_height):
                return
            visited.add((row, col))
            neighbors = [(-1,0), (1,0), (0,-1), (0,1)]
            for nbr in neighbors:
                dfs(row + nbr[0], col + nbr[1], heights[row][col], visited)
        

        overlap_array = []

        # Traverse through the first row and last row as these are the starting 
        # points from the two oceans
        for c in range(max_cols):
            dfs(0, c, heights[0][c], pacific)
            dfs(max_rows - 1, c, heights[max_rows - 1][c], atlantic)
        
        # Repeat this for the first col and last col 
        for r in range(max_rows):
            dfs(r, 0, heights[r][0], pacific)
            dfs(r, max_cols - 1, heights[r][max_cols - 1], atlantic)
        
        # Finally we find the overlapping cells
        for r in range(max_rows):
            for c in range(max_cols):
                if (r,c) in pacific and (r,c) in atlantic: 
                    overlap_array.append([r, c])
        return overlap_array

pa = Solution().pacificAtlantic
print(pa([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
print(pa([[1]]))

# Time Complexity : O(M*N)
# Space Complexity: O(M*N)