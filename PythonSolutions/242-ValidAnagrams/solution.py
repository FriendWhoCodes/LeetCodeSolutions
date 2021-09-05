# https://leetcode.com/problems/valid-anagram/

# TODO Proper function
# Implement it when you've added a sort function for strings and then using it






# Bad python sorted function based solution, can't use in interviews, unless implement own sort function
# O(nlogn) since sorted uses quick sort internally

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            return sorted(list(s)) == sorted(list(t))
        
