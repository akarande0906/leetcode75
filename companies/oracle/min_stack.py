'''
LC 155: Min Stack
'''
class MinStack:

    def __init__(self):
        self.stack = []

    # At every push the top of the stack will contain the pushed element and the min element 
    # at that point we always push the current val and the min element at that point
    # That way when the element is popped and if that is the min element, we know what the next 
    # min element is from the next element on top of the stack
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = self.stack[-1][1]
            self.stack.append((val, min(current_min, val)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()  
minStack.push(-2) # -2
minStack.push(0) # -2 0 
minStack.push(-3); # -2 0 -3
print(minStack.getMin()) # return -3
minStack.pop()
print(minStack.top())    # return 0
print(minStack.getMin()) # return -2