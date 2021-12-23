#   https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
                
        word1 = list(words[0])
                
        for word in words[1:] :
            new_word = []
            for char in word:
                if char in word1:
                    new_word.append(char)
                    word1.remove(char)
            word1 = new_word
        
        return word1
            
        
