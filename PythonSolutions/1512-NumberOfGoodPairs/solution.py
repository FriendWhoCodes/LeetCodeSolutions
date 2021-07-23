# https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        n = len(nums)
        result = 0
        
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    result += 1
        
        return result
                    
            
        
