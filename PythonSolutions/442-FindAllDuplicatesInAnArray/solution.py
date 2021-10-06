# TODO Without extra space:



# With extra space, using hash table:

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = {}
        result = []
        
        for num in nums:
            if num not in freq:
                freq[num] = 1 
            else:
                freq[num] += 1
                result.append(num)
        return result
        
        
