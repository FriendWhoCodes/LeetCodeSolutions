# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        
        for char in s:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1
        print(freq)
        
        for index, char in enumerate(s):
            if freq[char] == 1:
                return index
        
        return -1
