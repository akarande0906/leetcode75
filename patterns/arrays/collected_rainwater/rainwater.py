'''
LC 42: Trapping Rain Water
Given an array of non-negative integers representing the height of bars, calculate how much water can be trapped after raining.
[ 3, 0, 1, 0, 4, 0, 2]
[4, 2, 0, 3, 2, 5]
'''
class Solution:
    def collectedWater(self, height: list[int]) -> int:
        lptr = 0
        rptr = len(height) - 1
        max_left = 0
        max_right = 0
        total_vol = 0
        while lptr < rptr:
          if height[lptr] < height[rptr]:
             max_left = max(max_left, height[lptr])
             total_vol += max_left - height[lptr]
             lptr += 1
          else:
             max_right = max(max_right, height[rptr])
             total_vol += max_right - height[rptr]
             rptr -= 1
        return total_vol

print(Solution().collectedWater([ 3, 0, 1, 0, 4, 0, 2]))
print(Solution().collectedWater([4, 2, 0, 3, 2, 5]))
print(Solution().collectedWater([3, 0, 2, 0, 1]))

# TC: O(n)
# SC: O(1) since we are not using any extra space other than a few variables.

