'''
Leet Code: 1249: Minimum Remove to Make Valid Parantheses
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', 
in any positions ) so that the resulting parentheses string is valid and return any valid string.
'''

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i, char in enumerate(s):
            if char == ')':
                if stack and stack[-1][1] == '(':
                    stack.pop()
                else:
                    stack.append((i, char))
            elif char == '(':
                stack.append((i, char))
        if not stack:
            return s
        ret_str = ''
        prev_i = -1
        for i, char in stack:
            if prev_i == -1:
                ret_str += s[:i] 
            else:
                ret_str += s[prev_i+1:i]
            prev_i = i
        if i < len(s) - 1:
            ret_str += s[i+1:]
        return ret_str
    
minRemove = Solution().minRemoveToMakeValid
print(minRemove('lee(t(c)o)de)'))
print(minRemove('a)b(c)d)'))
print(minRemove('))(('))
print(minRemove('abc'))