# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        row_zeroes = [False] * rows
        col_zeroes = [False] * cols
        
        
        # Find the row and col value where there are zeroes in the row and column
        # Then update the row_zeroes and col_zeroes boolean arrays for that
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    col_zeroes[col] = True
                    row_zeroes[row] = True
        
        # If row or col value is zero in the boolean arrays, 
        # Then for those rows and cols make the elements zero
        for row in range(rows):
            for col in range(cols):
                if row_zeroes[row] or col_zeroes[col] :
                    matrix[row][col] = 0
