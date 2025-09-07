class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        n = len(nums)
        s = n * (n+1)//2
        for i in nums:
            s -= i
        return s

sol = Solution()
print(sol.missingNumber([3,0,1]))
print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))
