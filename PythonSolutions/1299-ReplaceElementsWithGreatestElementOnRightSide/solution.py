# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/ 



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
            
               
                
                
        
