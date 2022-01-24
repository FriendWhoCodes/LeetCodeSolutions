# https://leetcode.com/problems/detect-capital/

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        capitals = 0
        
        for char in word:
            if char.isupper():
                capitals += 1
        
        if capitals == 0 or capitals == len(word):
            return True
        elif capitals == 1 and word[0].isupper():
            return True
        else:
            return False
        

