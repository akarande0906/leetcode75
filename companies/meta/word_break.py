'''
LC 139: Word Break
Given a string s and a dictionary of strings wordDict, return true 
if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.
'''
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)  # convert wordDict to a set for constant time lookup
        n = len(s)
        dp = [False] * (n+1)  # create an array dp of length n+1
        dp[0] = True  # empty string can be segmented into an empty sequence of words
    
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
    
        return dp[n]  # return the final answer
    
'''
Alternate solution: More efficient:
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)  # convert wordDict to a set for constant time lookup
        n = len(s)
        dp = [False] * (n+1)  # create an array dp of length n+1
        dp[n] = True  # empty string can be segmented into an empty sequence of words
    
        for i in range(n, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i : i+len(w)] == w:
                    # This is because we only set it to true if we were able to get a match earlier
                    dp[i] = dp[i+len(w)] 
                    if dp[i]:
                        break
    
        return dp[0]  # return the final answer

'''
    
isWordBreak = Solution().wordBreak
print (isWordBreak('leetcode', ['leet', 'code']))
print (isWordBreak('applepenapple', ['apple', 'pen']))
print (isWordBreak('catsandog', ["cats","dog","sand","and","cat"]))

'''
Time Complexity: O(n * m * k),m where n is characters in s, m is length of wordDict, k is average length of words in wordDict
'''