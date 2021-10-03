# https://leetcode.com/problems/matrix-diagonal-sum/

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
        
