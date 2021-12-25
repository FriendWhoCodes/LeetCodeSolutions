# https://leetcode.com/problems/three-divisors/

class Solution:
    def isThree(self, n: int) -> bool:
        
        count = 0
        
        for i in range(2, n+1):
            if n % i == 0:
                count += 1
        
        if count == 2:
            return True
        
