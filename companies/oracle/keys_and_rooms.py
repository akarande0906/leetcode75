'''
LC 841: Keys and Rooms
'''
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited, keys = set(), set()
        visited.add(0)
        keys.add(0)
        while keys:
            k = keys.pop()
            new_keys = rooms[k]
            for nk in new_keys:
                if nk not in visited:
                    visited.add(nk)
                    keys.add(nk)
        return len(visited) == len(rooms)
                
sol = Solution()
assert sol.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]) == False
assert sol.canVisitAllRooms([[1],[2],[3],[]]) == True