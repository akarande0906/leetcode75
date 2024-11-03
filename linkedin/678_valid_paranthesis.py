class Solution:
    def checkValidString(self, s: str) -> bool:
        open_stack = []
        asterix_stack = []
        for i, ch in enumerate(s):
            if ch == '(':
                open_stack.append(i)
            elif ch == '*':
                asterix_stack.append(i)
            else:
                if open_stack:
                    open_stack.pop()
                elif asterix_stack:
                    asterix_stack.pop()
                else:
                    return False
        while open_stack and asterix_stack:
            # If open brackets come after the asterix brackets then it cannot balance
            if open_stack.pop() > asterix_stack.pop():
                return False
        if open_stack and not asterix_stack:
            return False
        return True            
            

print(Solution().checkValidString('((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()'))
print(Solution().checkValidString('(*))'))
print(Solution().checkValidString(')'))
print(Solution().checkValidString('('))

''' Alternative solution: Two pointer: O(n)
class Solution:
    def checkValidString(self, s: str) -> bool:
        open_count = 0
        close_count = 0
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '*':
                open_count += 1
            else:
                open_count -= 1
            if s[len(s) - i - 1] == ')' or s[len(s) - i - 1] == '*':
                close_count += 1
            else:
                close_count -= 1
            if open_count < 0 or close_count < 0:
                return False
        return True

'''
