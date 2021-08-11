# https://leetcode.com/problems/sorting-the-sentence/

import re
class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        
        # def last_letter(word):
        #     return word[::-1]
        # Instead making anonymous function that gets x[-1] i.e. last element
        # And uses it as a key for the sorted function
        # Sorted function returns a sorted list, we override the original list with sorted list
        
        words = sorted(words, key= lambda x : x[-1])
        
        result = []
        for word in words:
            result.append(re.sub(r'\d+', '', word))
        
        return ' '.join(result)
