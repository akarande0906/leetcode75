class Solution:
    def getMaxLen(self, nums: list[int]) -> int:
        ans = pos = neg = 0
        for num in nums:
            if num > 0:
                # Increment negative as well to track updates to negative
                pos = 1 + pos
                neg = 1 + neg if neg else 0
            elif num < 0:
                pos, neg = 1 + neg if neg else 0, 1 + pos
            else:
                pos = neg = 0
            ans = max(ans, pos)
        return ans

print (Solution().getMaxLen([0,1,-2,-3,-4]))
print (Solution().getMaxLen([-1,-2,-3,0,1]))


