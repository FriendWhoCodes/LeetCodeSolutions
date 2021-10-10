# https://leetcode.com/problems/bitwise-and-of-numbers-range/

# Wrong Answer

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        num = left
        result = 1
        
        while num <= right:
            result = num & (num + 1)
            num = num + 1
        
        return result
            
        
        
