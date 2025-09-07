'''
LC 921: Minimum Add to Make Parentheses Valid
Example: Input: s = "())" Output: 1
Input: s = "(((" Output: 3
'''
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        total = 0
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if not stack or stack[-1] != '(':
                    total += 1
                elif stack:
                    stack.pop()
        return total + len(stack)
    
minVal = Solution().minAddToMakeValid
print (minVal("((("))
print (minVal("())"))
print (minVal("(())))"))
print (minVal("(((())"))