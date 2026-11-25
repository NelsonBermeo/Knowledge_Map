# 155 Min Stack (medium)
# Design a stack that supports push, pop, top and retireving the minimum element in constant time


class MinStack(object):

    def __init__(self):
        self.stack = []
        self.curr_min = float("inf")
        self.len = 0

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)
        if value < self.curr_min:
            self.curr_min = value
        self.len += 1

    def pop(self):
        """
        :rtype: None
        """
        if self.len <= 0:
            return None  # Error
        else:
            if 
            self.stack.pop()
            self.len -= 1

    def top(self):
        """
        :rtype: int
        """
        if self.len <= 0:
            return None  # Error
        else:
            self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
