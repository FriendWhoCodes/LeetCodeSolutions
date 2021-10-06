# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

# With extra space

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        freq = {}
        result = []
        n = len(nums)
        
        temp = range(1, n + 1)
        
        
        for num in nums:
            if num not in freq:
                freq[num] = 1
                
        for num in temp:
            if num not in freq:
                result.append(num)
        
        return result
        
        
