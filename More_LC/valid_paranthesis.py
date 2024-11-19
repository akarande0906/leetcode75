'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brace_hash = {')':'(', '}':'{', ']':'['}
        stack = []
        stack.append(s[0])
        for c in range(1, len(s)):
            if s[c] in brace_hash:
                if len(stack) and brace_hash[s[c]] == stack[-1]:
                    stack.pop()
                else:
                    return False 
            elif c not in brace_hash:
                stack.append(s[c])
        return not stack
    
isValid = Solution().isValid
print (isValid('()[]{}'))
print (isValid('([])'))
print (isValid('(]'))