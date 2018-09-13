class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.tmp = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        for i in range(len(self.stack)):
            self.tmp.append(self.stack.pop())
        data = self.tmp.pop()
        for i in range(len(self.tmp)):
            self.stack.append(self.tmp.pop())
        return data

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        for i in range(len(self.stack)):
            self.tmp.append(self.stack.pop())
        data = self.tmp.pop()
        self.stack.append(data)
        for i in range(len(self.tmp) - 1):
            self.stack.append(self.tmp.pop())
        return data
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

myQueue = MyQueue()
myQueue.push(1)
myQueue.push(2)
print(myQueue.peek())
print(myQueue.pop())
print(myQueue.empty())
