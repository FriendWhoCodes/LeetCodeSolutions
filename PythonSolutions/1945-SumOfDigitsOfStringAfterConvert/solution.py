# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/submissions/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        # print(ord("a") - 96)
        # print(ord("z") - 96)
        temp = ""
        for char in s:
            temp += str((ord(char)-96))

        total = int(temp)
        
        while k:            
            total = self.find_sum(total)
            k -= 1
        
        return total
        
    
    def find_sum(self, num):
        total = 0
    
        while num:
            temp = num % 10
            total += temp
            num = num // 10

        return total

        
