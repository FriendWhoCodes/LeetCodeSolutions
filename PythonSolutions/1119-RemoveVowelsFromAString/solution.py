# https://leetcode.com/problems/remove-vowels-from-a-string/

class Solution:
    def removeVowels(self, s: str) -> str:
        result = ""
        
        vowels = ["a", "e", "i", "o", "u"]
        
        for char in s:
            if char not in vowels:
                result += char
        return result
        
