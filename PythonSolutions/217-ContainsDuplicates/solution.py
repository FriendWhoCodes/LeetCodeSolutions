
# O(n) time and O(n) space solution with a hash table

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        freq = {}
        
        for num in nums:
            if num not in freq:
                freq[num]  = 1
            else:
                return True
        
        return False
            
        
