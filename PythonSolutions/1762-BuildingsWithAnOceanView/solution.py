class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        
        index = len(heights) - 1
        result = []
        tallest = heights[index]
        result.append(index)
        
        while ( index >= 0):
            if heights[index] > tallest:
                result.append(index)
                tallest = heights[index]
            index -= 1
        result.sort()
        
        return result
        
