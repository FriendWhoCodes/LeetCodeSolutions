# https://leetcode.com/problems/valid-mountain-array/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        i = 0
        j = n = len(arr) - 1
        
        while i < j and arr[i] < arr[i + 1]:
            i += 1
        while j > 0 and arr[j] < arr[j - 1]:
            j -= 1
            
        if i == j and j != n and i != 0:
            return True
        else:
            return False
            
        
        
        
        
        
        
# Didn't clear all the test cases:
#         maximum = max(arr)
        
#         i = 0
#         j = len(arr) - 1
#         while (i < len(arr) and j >= 0 and arr[i] != maximum and arr[j] != maximum) :
#             if arr[i] > maximum or arr[j] > maximum:
#                 return False
#             else:
#                 i += 1
#                 j -= 1
        
