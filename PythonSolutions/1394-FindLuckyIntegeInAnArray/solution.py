# https://leetcode.com/problems/find-lucky-integer-in-an-array/

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        freq = {}
        
        for num in arr:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        result = []
        for key,value in freq.items():
            if key == value:
                result.append(key)
        
        if len(result) > 0:
            return max(result)
        
        else:
            return -1
