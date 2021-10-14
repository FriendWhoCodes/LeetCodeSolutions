# https://leetcode.com/problems/search-a-2d-matrix/ 

# TODO Optimized solution, directly applying Binary Search on the 2D matrix

# Bruteforce solution: With O(n^2) time and O(n) space

# Since the matrix is sorted, you can convert it to one dimensional array and then apply Binary Search
# O(n) space for 1D array and O(n^2) time to convert 2D array into 1D array

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        array = [0]* (m*n)
        
        k = 0
        for i in range(m):
            for j in range(n):
                array[k] = matrix[i][j]
                k += 1
        
        return self.bin_search(array, target)
    
    
    def bin_search(self, array, target):
        low = mid = 0
        high = len(array) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if target == array[mid]:
                return True
            elif target < array[mid]:
                    high = mid - 1
            else:
                low = mid + 1
        return False
                
        
