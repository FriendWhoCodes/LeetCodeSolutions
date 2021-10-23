# https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        
        for num in range(n+1):
            result.append(self.count_set(num))
    
        return result
    
    
    def count_set(self, n):
        set_bits = 0
        
        while n:
            n &= (n - 1)
            set_bits += 1
            n >>= 1
        
        return set_bits
        
