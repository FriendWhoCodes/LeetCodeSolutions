# https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/

class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        
        max_weight = 5000
        n = len(weight)
        
        weight.sort()
        
        total = 0
        count = 0
        i = 0
        
        while total < max_weight and i < n:
            total += weight[i]
            i += 1
            count += 1
        
        if total > max_weight:
            count -= 1
        
        return count
        
        
