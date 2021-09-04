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

    
    # Actually Fails since it returns the last occurrence of any chracter: e.g. for "aabb" returns 1 which is the index of last a, even though it's clearly repeated
    # Bruteforce Approach
    # Pick a character then check the rest of the string if it exists or not
    # If it exists, pick the next character else return this character

class Solution:
    def firstUniqChar(self, s: str) -> int:
        index = -1
        
        for i in range(len(s)):
            exists = False
            for j in range(i+1, len(s)):
                if s[j] == s[i]:
                    exists = True
            if exists == False:
                index = i
                break
        
        return index
