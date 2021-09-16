# https://leetcode.com/problems/baseball-game/


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
        
