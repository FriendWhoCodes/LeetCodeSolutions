# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/ 

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        length = len(arr) 
    
        right_max = arr[length -1]
        arr[length - 1] = -1
        
        i = length - 2
        while (i >= 0):
            temp = arr[i]
            
            arr[i] = right_max
            
            if right_max < temp:
                right_max = temp
            i -= 1
        
        return arr
            
            



# Bruteforce Method, time limit excceeds on LeetCode:


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(len(arr)):
            maximum = -1
            for j in range(i + 1, len(arr)):
                if maximum < arr[j]:
                    maximum = arr[j]
            arr[i] = maximum
        return arr
            
               
                
                
        
