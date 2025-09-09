'''
Leetcode 155: Min Stack

Implement the MinStack class:

MinStack() initializes the stack object.
push(int val) pushes the element val onto the stack.
pop() removes the element on the top of the stack.
top() gets the top element of the stack.
getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
'''
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack: # Maintain the value and the min val at this stage on the stack
            self.stack.append((val, val)) 
        else:
            cur_min = self.stack[-1][1] # Get the current min on the stack
            self.stack.append((val, min(val, cur_min))) # If val is lesser than cur_min, we update the cur_min at this point

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
obj.top()
print(obj.getMin())

