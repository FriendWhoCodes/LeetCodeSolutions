# https://leetcode.com/problems/maximum-number-of-balloons/

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = [ "b", "a", "l", "l", "o", "o", "n"]
        
        if len(text) < len(balloon):
            return 0
        
        freq = {} 
        
        for i in text:
            if i in balloon:
                if i not in freq:
                    freq[i] = 1
                else:
                    freq[i] += 1
                    
        for i in balloon:
            if i not in freq:
                return 0


        b = freq['b']
        a = freq['a']
        n = freq['n']
        
        
        l = freq['l']
        o = freq['o']
        
        return min (min(b, a, n), min (l, o) // 2)
        
        
       
       
        
        
        
