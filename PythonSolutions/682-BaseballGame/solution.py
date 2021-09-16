# https://leetcode.com/problems/baseball-game/

# The trick here is the negative number that you'd face in the ops array and how to check if it is negative or not.
# string.isdigit() does not work for negative numbers or float, so I implemented mine in a try except block.
# Used try except because otherwise int would give an error

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record = []
                        
        for i in range(len(ops)):
            if self.is_int(ops[i]):
                record.append(int(ops[i]))
            elif ops[i] == "+":
                record.append(int(record[-1]) + int(record[-2]))
            elif ops[i] == "D":
                record.append(2 * int(record[-1]))
            elif ops[i] == "C":
                record.pop()
        
        return sum(record)
    
    def is_int(self, s):
        is_int = True
        
        try:
            int(s) 
        except:
            is_int = False
        
        return is_int
        
