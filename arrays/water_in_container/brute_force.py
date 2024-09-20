class Solution:
    def maxArea(self, height: list[int]) -> int:
        num = len(height)
        marea = 0
        for n in range(0, num-1):
            for m in range(n, num):
                area = min(height[n], height[m]) * (m - n)
                marea = max(marea, area)
        return marea

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
print(sol.maxArea([1,1]))
