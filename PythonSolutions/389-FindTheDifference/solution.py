# https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        freq = {}
        freq2 = {}
        
        # Should do it with dict instead of these two loops
        # That's more readable
        for char in t:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1
        
        for char in s:
            if char not in freq2:
                freq2[char] = 1
            else:
                freq2[char] += 1
        
        for char in t:
            if char not in s:
                return char
            else:
                if freq[char] > freq2[char]:
                    return char
            
            
        
