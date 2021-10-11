# https://leetcode.com/problems/reshape-the-matrix/

from collections import deque
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        if len(mat) == 0:
            return mat
        
        m = len(mat)
        n = len(mat[0])
        
        # If original and expected array have differentnumber of elements,
        # Return original array
        if m*n != r*c:
            return mat
        
        # This fails for whatever reason, couldn't figure out so initializing later with list comprehension
        # result = [[0]*c]*r
        # print(result)
        
        # Initialize the queue
        queue = deque()
        
        # Populate the queue, with row by row traversal of original matrix
        for i in range(m):
            for j in range(n):
                queue.append(mat[i][j])
        
        # Initialize the result matrix
        result = [[0 for _ in range(c)] for _ in range(r)]
        print(result)
 
        # Populate the result matrix with values from the queue        
        for i in range(r):
            for j in range(c):
                result[i][j] = queue.popleft()
                # print(result[0])

        
        return result
        
        
        
