'''
Leetcode 22: Generate Parenthesis
'''
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        gen_brackets = []
        def generateBrackets(bracket_str, left, right):
            if len(bracket_str) == 2 * n: # Since the brackets are balanced, we will get 2 times the number 
                gen_brackets.append(''.join(bracket_str))
            if left < n: # Execute this till we have as many left brackets as intended
                bracket_str.append('(')
                generateBrackets(bracket_str, left+1, right)
                bracket_str.pop()
            if right < left: # Execute this till we have as many right brackets as we have left brackets. This will balance the brackets
                bracket_str.append(')')
                generateBrackets(bracket_str, left, right+1)
                bracket_str.pop()
        
        generateBrackets([], 0, 0)
        return gen_brackets
    

gen = Solution().generateParenthesis
print(gen(3))
print(gen(4))