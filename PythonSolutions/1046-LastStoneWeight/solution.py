class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            stones.sort()
            max1, max2 = stones[-1], stones[-2]
        
            if max1 == max2:
                stones.remove(max1)
                stones.remove(max2)
            elif max1 < max2:
                stones.remove(max1)
                stones[-2] = max2 - max1
            elif max2 < max1:
                stones.remove(max2)
                stones[-1] = max1 - max2
        
        if len(stones) >= 1:
            
            return min(stones)
        else:
            return 0
                
                
                
            
