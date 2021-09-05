# https://leetcode.com/problems/min-stack/


# Using tuple to store min value so far for each element:


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, val: int) -> None:
        if self.is_empty():
            self.stack.append((val, val))
        else:
            minimum = self.stack[-1][1]
            self.stack.append((val, min(val,minimum)))
        

    def pop(self) -> None:            
        if self.is_empty():
            return
        else:
            self.stack.pop()
        

    def top(self) -> int:
        if self.is_empty():
            return -1
        else:
            return self.stack[-1][0]
    
    def is_empty(self):
        return len(self.stack) == 0
        

    def getMin(self) -> int:
        if not self.is_empty():
            return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
