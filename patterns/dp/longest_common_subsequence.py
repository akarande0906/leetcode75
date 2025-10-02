'''
Leetcode 1143: Longest Common Subsequence 
'''
class Solution:
    # Traverse in a grid where the row 0 is text1 and col 0 is text2
    # Compare chars, if matched, move diagonally to compare the next set, 
    # else compare by skipping a char from each word and taking the max
    '''
        a b c d e
    a
    b
    c
    '''
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text1) + 1)] for j in range(len(text2) + 1)]
        for j in range(1, len(text2) + 1):
            for i in range(1, len(text1) + 1):
                # If the characters match, we add one to the value of the j-1 and i-1 th char
                if text1[i-1] == text2[j-1]:
                    dp[j][i] = 1 + dp[j-1][i-1]
                else:
                    dp[j][i] = max(dp[j-1][i], dp[j][i-1])
        return dp[j][i]


lcs = Solution().longestCommonSubsequence
print(lcs("abcde", "ace"))
print(lcs("abc", "abc"))
print(lcs("abc", "def"))
print(lcs("abc", "adbecfd"))