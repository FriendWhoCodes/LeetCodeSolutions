# https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        
        if num == 0:
            return 0
        
        else:
            while self.count_digits(num) != 1:
                num = self.find_sum(num)
        
            return num
    
    def find_sum(self, num):
        total = 0
        
        while num:
            temp = num % 10
            total += temp
            num = num // 10
        
        return total
    
    def count_digits(self, num):
        count = 0
        while num:
            count += 1
            num = num // 10
        
        return count
