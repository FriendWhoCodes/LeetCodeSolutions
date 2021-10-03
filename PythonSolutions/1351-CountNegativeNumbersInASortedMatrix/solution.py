# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

# Bruteforce solution, not utilizng sorted elements part

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        negatives = 0
        
        for row in grid:
            for val in row:
                if val < 0:
                    negatives += 1
        
        return negatives
        
        
        
        
        
