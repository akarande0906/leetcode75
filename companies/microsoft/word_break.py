'''
Leetcode 139: Word Break
'''
from typing import List

class Solution:
    def wordBreak(self, s: str, wordList: List[str]) -> bool:
        wordDict = set(wordList) # Allows for O(1) lookup
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True
        for i in range(n, -1, -1):
            for w in wordDict:
                if i + len(w) <= n and s[i : i+len(w)] in wordDict:
                    dp[i] = dp[i+len(w)]
                    if dp[i]:
                        break # We found a match
        return dp[0]
    

isBreak = Solution().wordBreak
print(isBreak("leetcode", ["leet","code"]))
print(isBreak("applepenapple", ["apple","pen"]))
print(isBreak("catsandog", ["cats","dog","sand","and","cat"]))


        