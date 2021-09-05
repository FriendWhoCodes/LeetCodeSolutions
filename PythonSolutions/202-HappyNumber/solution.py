# https://leetcode.com/problems/happy-number/


# Improved Solution


# My Initial solution
class Solution:
    def isHappy(self, n: int) -> bool:
        
        temp = n
        freq = {}
        while (temp != 1):
            temp = self.sum_square_digits(temp)
            if temp not in freq:
                freq[temp] = 1
            else:
                return False
            if temp == n:
                return False
            
        if temp == 1:
            return True
        else:
            return False
            
        
        
    def sum_square_digits(self, n: int) -> int:
        sum = 0
        
        while n > 0:
            temp = n % 10
            sum += temp * temp
            n = n // 10
        
        return sum
