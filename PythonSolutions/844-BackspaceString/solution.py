# Use a stack and pop off the top character whenever there is a # i.e. backspace

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
       return self.final_string(s) == self.final_string(t)
    
    def final_string(self, s):
        stack = []
        for i in s:
            if i != "#":
                stack.append(i)
            elif len(stack) > 0:
                stack.pop()
        return ''.join(stack)
            
        
