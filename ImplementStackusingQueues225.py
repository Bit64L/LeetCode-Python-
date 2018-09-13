class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        try:
            import queue
        except ImportError:
            import Queue as queue
        self.q = queue.Queue()
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q.put(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        for i in range(self.q.qsize() - 1):
            self.q.put(self.q.get())
        return self.q.get()
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        for i in range(self.q.qsize() - 1):
            self.q.put(self.q.get())
        tmp = self.q.get()
        self.q.put(tmp)
        return tmp

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.q.empty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
myStack = MyStack()
myStack.push(1)
myStack.push(2)
print(myStack.top())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.empty())
