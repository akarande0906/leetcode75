''' Leet Code: 516
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
'''
class Solution:
    def longestPalindromicSubsequence(self, text: str) -> int:

        def longestCommonSubsequence(text1: str, text2: str) -> int:
            dp = [[0 for i in range(len(text1) + 1)] for j in range(len(text2) + 1)]
            arr = []
            for j in range (len(text2) - 1, -1, -1):
                for i in range (len(text1) - 1, -1, -1):
                    if text1[i] == text2[j]:
                        dp[j][i] = 1 + dp[j+1][i+1]
                        arr.append(text2[j])
                    else:
                        dp[j][i] = max(dp[j+1][i], dp[j][i+1])
            print (arr)
            return dp[0][0]
        return longestCommonSubsequence(text, text[::-1])

lps = Solution().longestPalindromicSubsequence
print(lps('abcde'))
print(lps('bbbab'))
print(lps('abcxyzcba'))



