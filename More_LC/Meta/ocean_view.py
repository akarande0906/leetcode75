'''
LC 1762: Buildings with Ocean View
There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.
The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. 
Formally, a building has an ocean view if all the buildings to its right have a smaller height.
Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.
'''
class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        n = len(heights)
        comparison = []
        comparison.append(n-1)
        max_height = heights[n-1]
        for b in range(n - 2, -1, -1):
            if heights[b] > max_height:
                comparison.append(b)
                max_height = heights[b]
        return comparison[::-1]
    
print (Solution().findBuildings([4,2,3,1]))
print (Solution().findBuildings([4,3,2,1]))
print (Solution().findBuildings([1,3,2,4]))


