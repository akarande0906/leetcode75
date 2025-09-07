'''
LC 11: Container With Most Water
'''
class Solution:
    def maxArea(self, height: list[int]) -> int:
        marea = 0
        l = 0
        r = len(height) - 1
        while  l < r:
            area = min(height[l], height[r]) * (r - l)
            marea = max (area, marea)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return marea

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
print(sol.maxArea([1,1]))
        
