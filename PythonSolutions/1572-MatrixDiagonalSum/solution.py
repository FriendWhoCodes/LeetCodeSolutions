# https://leetcode.com/problems/matrix-diagonal-sum/

# TODO an O(n) solution


# Note how the primary diagonal is simply indices with same value i.e. i == j
# Note how secondary diagonal is indices with changing value for both i and j. With i from 0 and j from len(mat) - 1 to i increasing to len(mat) - 1 and j decreasing to 0
# i.e. secondary diagonal goes from mat[0][len(mat)-1] to mat[len(mat) - 1][0].
# Here we ignore the i ==j part in second diagonal, since it's already counter in first diagonal.

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        pri_diagonal = 0
        sec_diagonal = 0
        
        for i in range(len(mat[0])):
            for j in range(len(mat[0])):
                if i == j:
                    pri_diagonal += mat[i][j]
                
        
        i, j = 0, len(mat[0]) - 1
        
        while i <= len(mat[0]) - 1 and j >= 0:
                if i != j :
                    sec_diagonal +=  mat[i][j]
                i += 1
                j -= 1
                
        
        
        return pri_diagonal + sec_diagonal
        
# Another solution with both diagonals being calculated within one outer while loop

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        rows = len(mat)
        cols = len(mat[0])
        
        i, j = 0, 0
        dia1 , dia2 = 0, 0
        k = cols - 1
        
        while i < rows and k >= 0:
            while j < cols:
                if i == j:
                    dia1 += mat[i][j]
                j += 1
            
            if i != k:
                dia2 += mat[i][k]
            k -= 1
            j = 0
            i += 1
        
        return dia1 + dia2
            
