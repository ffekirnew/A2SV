class MyQueue(object):

    def __init__(self):
        self.list = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.list.insert(0, x)
        

    def pop(self):
        """
        :rtype: int
        """
        if self.list == []: return None
        else: return self.list.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        if self.list == []: return None
        else: return self.list[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return self.list == []
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()