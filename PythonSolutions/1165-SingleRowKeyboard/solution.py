# https://leetcode.com/problems/single-row-keyboard

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        
        letters = {}
        
        for index, key in enumerate(keyboard):
            if key not in letters:    
                letters[key] = index
        
        time = i =0
        
        for j in word:
            time += abs (i - letters[j])
            i = letters[j]
        
        
        return time
        
