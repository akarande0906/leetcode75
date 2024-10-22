class Solution:
    def __init__(self):
        self.stack = []
    def parseInteger(str):
        try:
             val = int(str)
        except:
             val = float('-inf')
        return val
            
    def revPolishNotation(self, polisharray):
        operationSet = {'+', '-', '/', '*'}
        result = 0
        for val in polisharray:
            print (self.stack)
            if not val in operationSet:
                self.stack.append(int(val))
            else:
                num2 = self.stack.pop()
                num1 = self.stack.pop()
                if val == '-':
                    result = num1 - num2
                elif val == '+':
                    result = num1 + num2
                elif val == '*':
                    result = num1 * num2
                elif val == '/':
                    result = int(num1 / num2)
                self.stack.append(result)
                    
        return result


print(Solution().revPolishNotation(["2","1","+","3","*"]))
print(Solution().revPolishNotation(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

