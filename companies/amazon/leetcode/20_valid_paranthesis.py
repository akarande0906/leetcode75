'''
LC 20: Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        brackets_map = {'}':'{', ']':'[', ')':'('}
        stack = []
        for char in s:
            if char not in brackets_map:
                # Opening braces
                stack.append(char)
            else:
                if stack:
                    if stack[-1] != brackets_map[char]:
                        return False
                    else:
                        stack.pop()
                else:
                    return False
        return not stack
# Time Complexity: O(n) where n is the length of the string
# Space Complexity: O(n) for the stack in the worst case when all characters are opening brackets
is_valid = Solution().isValid
print(is_valid("()"))          # True
print(is_valid("()[]{}"))      # True
print(is_valid("(]"))          # False
print(is_valid("([)]"))        # False