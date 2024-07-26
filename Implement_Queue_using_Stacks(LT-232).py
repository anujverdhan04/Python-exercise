from queue import LifoQueue

class MyQueue:

    def __init__(self):
        self.input = LifoQueue()
        self.output = LifoQueue()
        

    def push(self, x: int) -> None:
        while not self.input.empty():
            self.output.put(self.input.get())
        # Insert the desired element in the stack input
        self.input.put(x)
        # Pop out elements from the stack output and push them into the stack input
        while not self.output.empty():
            self.input.put(self.output.get())
        

    def pop(self) -> int:
        if self.input.qsize() == 0:
            raise IndexError("pop from empty queue")
        return self.input.get()


    def peek(self) -> int:
        if self.input.qsize() == 0:
            raise IndexError("peek from empty queue")
        return self.input.queue[-1]


    def size(self) -> int:
        return self.input.qsize()

    def empty(self) -> bool:
        return self.input.qsize() == 0

# Your MyQueue object will be instantiated and called as such:
#obj = MyQueue()
#obj.push(1)
#obj.push(2)
#print(obj.top())    # Output: 1
#print(obj.pop())    # Output: 1
#print(obj.empty())  # Output: False
#print(obj.pop())    # Output: 2
#print(obj.empty())  # Output: True
