# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        chars = list(chars)
        
        for word in words:
            temp = []
            chars_pool = chars[:]
            for char in word:
                if char not in chars_pool:
                    break
                else:
                    temp.append(char)
                    chars_pool.remove(char)
            temp = ''.join(temp)
            if temp == word:
                count += len(word)
                    
        return count
