# https://leetcode.com/problems/check-if-n-and-its-double-exist/




# Bruteforce approach:

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(1, len(arr)):
                if (i != j and (arr[i] == 2 * arr[j] or arr[i] == arr[j] / 2 )):
                    return True
        
