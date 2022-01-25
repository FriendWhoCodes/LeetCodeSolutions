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
 
 # My most recent solution that passed all test cases
 class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        n = len(arr)
        
        if n < 3:
            return False
        
        i = 0        
        maximum = max(arr)
        
        # Check first half of the array is strictly increasing

        while arr[i] < maximum and i < n - 1:
            if arr[i] < arr[i+1]:
                i += 1
                continue
            else:
                return False
        
        # If maximum is the last index of the array, then there is no downward slope
        # If maximum is the first index of the array, then there is no upward slope
        # So not a mountain array, so return False
        if i == n - 1 or i == 0:
            return False
        
        # Check second half of the array is strictly decreasing
        j = i
        while j < n - 1:
            if arr[j] > arr[j+1]:
                j += 1
                continue
            else:
                return False
        
        return True
                
                   
        
        
        
        
        
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
        
