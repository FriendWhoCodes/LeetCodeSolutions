# https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        mag_chars = {}
        ran_chars = {}
        
        for char in magazine:
            if char not in mag_chars:
                mag_chars[char] = 1
            else:
                mag_chars[char] += 1
        
        for char in ransomNote:
            if char not in ran_chars:
                ran_chars[char] = 1
            else:
                ran_chars[char] += 1
        
        for char in ransomNote:
            if char not in mag_chars:
                return False
            elif ran_chars[char] > mag_chars[char]:
                return False
            
        return True
            
                
        
        
                
        
        
            
        
