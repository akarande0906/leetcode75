''' Leet Code: 1143
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text1) + 1)] for j in range(len(text2) + 1)]
        arr = []
        '''
        for j in range(1, len(text2) + 1):
            for i in range(1, len(text1) + 1):
                if text1[i-1] == text2[j-1]:
                    arr.append(text1[i-1])
                    dp[j][i] = 1 + dp[j-1][i-1]
                else:
                    dp[j][i] = max(dp[j-1][i], dp[j][i-1])
        print (''.join(arr))
        return dp[j][i]
        '''

        for j in range (len(text2) - 1, -1, -1):
            for i in range (len(text1) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[j][i] = 1 + dp[j+1][i+1]
                    arr.append(text2[j])
                else:
                    dp[j][i] = max(dp[j+1][i], dp[j][i+1])
        print (''.join(reversed(arr)))
        return dp[0][0]

lcs = Solution().longestCommonSubsequence
print(lcs('abcde', 'ace'))
print(lcs('bcde', 'ace'))



