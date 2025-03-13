'''
LC 300: Longest Increasing Subsequence
'''
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1] * n # As for each element by itself it can be seq of 1
        # See if we can keep adding to the sequence
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
    # TC : O(n^2)
    # SC : O(n)

lengthOfLIS = Solution().lengthOfLIS
print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([0,1,0,3,2,3]))
print(lengthOfLIS([7,7,7,7,7,7,7]))
print(lengthOfLIS([4,10,4,3,8,9]))

