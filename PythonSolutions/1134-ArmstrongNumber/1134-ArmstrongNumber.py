import math
class Solution:
    def isArmstrong(self, n: int) -> bool:
        
        cube_sum = temp = power = 0
        num1 = num2 = n
        
        while num1 != 0:
            power += 1
            num1 = num1 // 10
        
        while num2 != 0: 
            temp =  num2 % 10
            cube_sum += temp ** power
            num2 = num2 // 10
        if n == cube_sum:
            return True
            
