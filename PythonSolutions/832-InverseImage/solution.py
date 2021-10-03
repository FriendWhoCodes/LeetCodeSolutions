# Flip an image horizontally
# Then flip 0 and 1
# Time: O(n^2) and Space: O(n^2)

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        result = []
        
        # First flip matrix
        for row in image:
            result.append(row[::-1])
        
        # Then inverse matrix
        for i in range(len(result)):
            for j in range(len(result)):
                if result[i][j] == 0:
                    result[i][j] = 1
                elif result[i][j] == 1:
                    result[i][j] = 0
        
        return result
        
        
