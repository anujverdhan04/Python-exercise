class MinStack:

    def __init__(self):
        self.stack = []      # Main stack to store the elements
        self.min_stack = []  # Stack to store the minimum elements
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        
    def pop(self) -> None:
        if self.stack:
            top = self.stack.pop()
            # If the popped element is the same as the top of the min_stack, pop it from min_stack as well
            if top == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        raise IndexError("top from empty stack")

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        raise IndexError("getMin from empty stack")


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()