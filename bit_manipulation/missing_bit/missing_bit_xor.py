class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        # With XOR a number xored with itself gives 0
        # So we XOR till we get the missing number
        for i in range(1, n + 1):
            ans ^= i
        for num in nums:
            ans ^= num
        return ans

sol = Solution()
print(sol.missingNumber([3,0,1]))
print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))
