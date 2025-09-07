class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True # Base case
        '''
        for i in range(len(s) -1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i : i+len(w)] == w:
                    dp[i] = dp[i+len(w)] # This is because we only set it to true if we were able to get a match earlier
                if dp[i]:
                    break
        '''
        for i in range(len(s)):
            for w in wordDict:
                if s[i-len(w)+1:i+1] == w:
                    if i - len(w) == -1:
                        dp[i] = True
                    else:
                        dp[i] = dp[i-len(w)]
                if i == len(s) - 1 and dp[i] == True:
                    return True
        return False


print (Solution().wordBreak('leetcode', ['leet', 'code']))
print (Solution().wordBreak('pineappleapplepen', ['apple', 'pine', 'pen', 'pineapple']))
print (Solution().wordBreak('cowsareblue', ['cow', 'cows', 'are', 'blue', 'sare']))
print (Solution().wordBreak('ilikesamsung', ["mobile", "samsung", "sam", "sung", "man", "mango", "icecream", "and", "go", "i", "like", "ice", "cream"]))

