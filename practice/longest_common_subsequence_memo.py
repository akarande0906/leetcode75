''' Leet Code: 1143
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1 for i in range(len(text1) + 1)] for j in range(len(text2) + 1)]
        
        def helper(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if memo[j][i] != -1:
                return memo[j][i]
            if text1[i] == text2[j]:
                memo[j][i] = 1 + helper(i+1, j+1)
            else:
                memo[j][i] =  max(helper(i, j+1), helper(i+1, j))
            print (memo[j][i])
        return helper(1, 1)

lcs = Solution().longestCommonSubsequence
print(lcs('abcde', 'ace'))
print(lcs('bcde', 'ace'))



