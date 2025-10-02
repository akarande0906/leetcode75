'''
Leetcode 150: Evaluate Reverse Polish Notation
'''
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {'+', '-', '*', '/'}
        for t in tokens:
            if t in operations:
                # Fetch the last two elements off the stack
                second, first = stack.pop(), stack.pop()
                value = None
                if t == '+':
                    value = first + second
                elif t == '-':
                    value = first - second
                elif t == '/':
                    # This is done because python's negative integer division always floors towards neg infinity
                    # unlike positive division which fllors towards zero.
                    value = abs(first) // abs(second)
                    if (first < 0 and second > 0) or (first > 0 and second < 0):
                        value = -value
                else:
                    value = first * second
                stack.append(value)
            else:
                stack.append(int(t))
        return stack[-1]
    
evalRPN = Solution().evalRPN
print(evalRPN(["2","1","+","3","*"]))
print(evalRPN(["4","13","5","/","+"]))
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
    
