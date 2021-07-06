class Solution:
    def isArmstrong(self, n: int) -> bool:
        
        power = total = 0
        temp1 = temp2 = n
        
        while temp1 != 0:
            power += 1
            temp1 = temp1 // 10
            
        while temp2 !=0:
            digit =  temp2 % 10
            total += digit ** power
            temp2 = temp2 // 10
        
        if total == n:
            return True
        
