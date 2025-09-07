'''
LC 755: Pour Water
'''
class Solution:
    def pourWater(self, heights: list[int], volume: int, k: int) -> list[int]:
        for _ in range (volume):
            water_position = k # Start here
            for i in reversed(range(k)): # First go left
                if heights[i] < heights[i+1]:
                    water_position = i
                elif heights[i] > heights[i+1]:
                    break
            if water_position == k: # Go right
                for i in range(k+1, len(heights)):
                    if heights[i-1] > heights[i]:
                        water_position = i
                    elif heights[i-1] < heights[i]:
                        break
            heights[water_position] += 1
        return heights

sol = Solution()
print(sol.pourWater([2,1,1,2,1,2,2], 4, 3)) # [2,2,2,3,2,2,2]
print(sol.pourWater([1,2,3,4], 2, 2)) # [2,3,3,4]
print(sol.pourWater([3,1,3], 5, 1)) # [4,4,4]
print(sol.pourWater([1,2,3,4,3,2,1], 5, 3)) # [3,4,4,4,3,2,1]
print(sol.pourWater([1,2,3,4,3,2,1], 7, 3)) # [4,4,4,4,3,2,2]

# Time Complexity: O(volume * n)
# Space Complexity: O(1) # We are not allotting any extra space. We are modifying the list in place.
                

