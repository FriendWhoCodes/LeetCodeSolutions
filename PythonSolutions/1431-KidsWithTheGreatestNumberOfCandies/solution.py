# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        result = []
        max_current = max(candies)
        
        for i in candies:
            if (i + extraCandies) >= max_current:
                result.append(True)
            else:
                result.append(False)
        
        return result
            
            
            
        
        
        
