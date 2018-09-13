class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        import sys
        self.min = sys.maxsize
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.min > x:
            self.min = x
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        data = self.stack.pop()
        if data == self.min:
            if len(self.stack) == 0:
                self.min = sys.maxsize
            else:
                tgt = self.stack[0]
                for i in range(len(self.stack)):
                    if tgt > self.stack[i]:
                        tgt = self.stack[i]
                self.min = tgt
        return data
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack) - 1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
print(minStack.pop())
print(minStack.top())
print(minStack.getMin())

