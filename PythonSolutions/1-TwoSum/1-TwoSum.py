'''
1. Brute Force Approach: Run two loops and try with all possibilites. Except the cases where the number is repeated 
(e.g. in [1,5,5], answer is [1,2] and not [1,1] or [2,2] i.e. same index is not allowed and i and j must be different)

Runtime: 7736 ms, faster than 5.00% of Python3 online submissions for Two Sum.
Memory Usage: 14.9 MB, less than 39.53% of Python3 online submissions for Two Sum.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        
        for i in range(0, n):
            for j in range(1, n):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]
                    
    
    
    '''
    The optimized solution reduces complexity to linear time by using a hash table and adding two itearation to it:
    In first iteration we add the elements and their indeices to hash table and in the second iteration we look at diffrence or complement in the hash table.
    While making sure that we don't use the same index.
    If we find the difference in hash table, we return the value.
    
    Runtime: 7980 ms, faster than 5.00% of Python3 online submissions for Two Sum.
    Memory Usage: 14.8 MB, less than 39.53% of Python3 online submissions for Two Sum.
    '''
    
    class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}
        
        for i in range(len(nums)):
           dic.update({nums[i] : i})
        
        for i in range(len(nums)):
            comp = target - nums[i]
            
            if comp in dic and dic.get(comp) != i:
                return [i, dic.get(comp)]
        
                
            '''
            This can be further optimized by doing the check and update in one go.
            '''
        
        
        
