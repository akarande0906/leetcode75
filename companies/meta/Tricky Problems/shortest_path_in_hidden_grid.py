'''
LC 1778: Shortest Path in Hidden Grid
Return the minimum distance between the robot's initial starting cell and the target cell. 
If there is no valid path between the cells, return -1.
'''
from collections import deque

# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> None:
#        
#
#    def isTarget(self) -> bool:
#        
#

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        backtrack = {'U':'D', 'D':'U', 'L':'R', 'R':'L'}
        directions = [('U',-1,0), ('D',1,0), ('L',0,-1), ('R',0,1)]
        visited = set()
        visited.add((0,0))
        target = None

        # First run dfs to get all the valid paths. This will help us only 
        # follow these in the BFS
        def dfs(row, col):
            nonlocal target 
            if master.isTarget():
                target = (row, col)
            ans = False
            for dir, dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if not (new_row, new_col) in visited and master.canMove(dir):
                    master.move(dir)
                    visited.add((new_row, new_col))
                    dfs(new_row, new_col)
                    master.move(backtrack[dir]) # Backtrack once we cannot move any more
        # We assume that the starting cell is (0,0)
        dfs(0,0)
        if not target:
            return -1

        # We use BFS here as that will result in the shortest path. 
        queue = deque()
        queue.append((0, 0, 0))
        visited.remove((0,0)) 
        while queue:
            row, col, path_length = queue.popleft()
            if (row, col) == target:
                return path_length
            for dir, dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if (new_row, new_col) in visited: # Process only if row, col is in the path
                    queue.append((new_row, new_col, path_length+1))
                    visited.remove((new_row, new_col))
            
            
        return -1

# Time Complexity: O(V+E) where V is the number of vertices and E is the number of edges
# Space Complexity: O(V) where V is the number of vertices
