'''
LC 22: Generate Paranthesis
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # Permutation
        bracket_list = []
        def genRecur(bracket_str, left, right):
            if len(bracket_str) == 2 * n:
                bracket_list.append(''.join(bracket_str))
                return
            if left < n:
                bracket_str.append('(')
                genRecur(bracket_str, left+1, right)
                bracket_str.pop()
            if right < left:
                bracket_str.append(')')
                genRecur(bracket_str, left, right+1)
                bracket_str.pop()
        genRecur([], 0, 0)
        return bracket_list

gen_pan =  Solution().generateParenthesis
print (gen_pan(3))
print (gen_pan(4))  
    
# Time Complexity: O(4^n/sqrt(n)) where n is the number of pairs of paranthesis
# Space Complexity: O(4^n/sqrt(n)) as we are storing all the possible combinations of paranthesis


