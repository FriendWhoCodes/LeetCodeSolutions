# https://leetcode.com/problems/check-if-the-sentence-is-pangram/

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        freq = {}
        for char in sentence:
            if char not in freq:
                freq[char] = 1
        
        if sum(freq.values()) == 26:
            return True
        
