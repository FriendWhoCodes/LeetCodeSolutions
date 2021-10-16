# https://leetcode.com/problems/implement-queue-using-stacks/

# Solution with 2 stacks:

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        # When S1 is not empty:
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
            
        self.s1.append(x)
        
        # Push back s2 content to s1
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()
        

    def pop(self) -> int:
        if not self.empty():
            return self.s1.pop()
        

    def peek(self) -> int:
        if not self.empty():
            return self.s1[-1]
        

    def empty(self) -> bool:
        if len(self.s1) == 0:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
