class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.m = None

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.m = x if self.m == None else min(self.m, x)

    def pop(self) -> None:
        self.stack.pop(-1)
        if self.stack:
            self.m = min(self.stack)
        else:
            self.m = None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.m

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
