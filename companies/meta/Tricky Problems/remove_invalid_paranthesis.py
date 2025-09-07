'''
LC 301: Remove Invalid Parentheses
'''
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def getLeftAndRightCounts(s):
            l, r = 0, 0

            for c in s:
                if c == '(':
                    l += 1
                elif c == ')':
                    if l == 0:
                        r += 1
                    else:
                        l -= 1
            return l,r
        
        def isValid(s):
            count = 0
            for c in s:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                if count < 0:
                    return False
            return True
        ans = []

        def dfs(s, start, l, r):
            if not l and not r and isValid(s):
                ans.append(s)
            else:
                for i in range(start, len(s)):
                    if i > start and s[i] == s[i-1]:
                        continue
                    if r > 0 and s[i] == ')':
                        dfs(s[:i]+s[i+1:], i, l, r-1)
                    elif l > 0 and s[i] == '(':
                        dfs(s[:i]+s[i+1:], i, l-1, r)
        l, r = getLeftAndRightCounts(s)
        dfs(s, 0, l, r)
        return ans

# Time Complexity: O(2^N) where N is the length of the string
# Space Complexity: O(N) where N is the length of the string
checker = Solution().removeInvalidParentheses
print(checker("()())()")) # ["()()()", "(())()"]
print(checker("(a)())()")) # ["(a)()()", "(a())()"]
print(checker(")(")) # [""]

