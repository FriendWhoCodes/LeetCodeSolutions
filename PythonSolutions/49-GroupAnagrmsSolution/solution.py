# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sorted_dic = {}
        result = []
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            
            if sorted_word not in sorted_dic:
                sorted_dic[sorted_word] = [word]
            
            else:
                sorted_dic[sorted_word].append(word)
        
        for item in sorted_dic:
            result.append(sorted_dic[item])
        
        return result
            
        
