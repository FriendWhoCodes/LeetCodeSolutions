# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0] * length
        for i in range(len(nums)):
            temp_count = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    temp_count += 1
            result[i] = temp_count
        
        return result
            
                    
            
        
