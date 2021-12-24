# https://leetcode.com/problems/count-square-sum-triples/

class Solution:
    def countTriples(self, n: int) -> int:
        
        # c = sqrt(a*a + b* b)
        # Same as Pythagorean Triplets
        
        count = 0
        
        for a in range(1,n+1):
            for b in range(a+1, n+1):
                sqr = sqrt(a*a + b*b)
                if sqr <= n and int(sqr) == sqr:    # If the number is integer, then int(num) == num, since Pythaogrean triplets are whole numbers
                        count += 2                  # Increment by two since both (a,b) and (b,a) are solutions and count
        
        return count
            
        
        
        
