# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        
        maximum = 0
        temp = []
        for sentence in sentences:
            count = 0
            sent = sentence.split(" ")
            temp.append(sent)
        
        for item in temp:
            count = len(item)
            maximum = max(count, maximum)
            
        return maximum
        
