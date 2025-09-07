'''
LC 227: Basic Calculator II with precedence of * and /
'''
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        cur = 0
        op = '+'
        s = s.strip()
        for c in s + '+':
            if c == ' ':
                continue
            elif c.isdigit():
                cur = cur * 10 + int(c)
            else:
                if op == '-':
                    stack.append(-cur)
                elif op == '+':
                    stack.append(cur)
                elif op == '*':
                    stack.append(stack.pop() * cur)
                elif op == '/':
                    stack.append(int(stack.pop() / cur))
                cur, op = 0, c
        return sum(stack)
    

cal = Solution().calculate
print (cal("3+2*2"))
print (cal(" 3/2 "))
print (cal(" 3+5 / 2 "))
print (cal("3*5/2"))
print (cal("42"))
            
            