# https://leetcode.com/problems/decompress-run-length-encoded-list/

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        
        i = 1
        while (i < n):
            freq = nums[i - 1]
            val = nums[i]
            
            temp_list = [val] * freq
            result.extend(temp_list)
            i = i + 2
        return result
            
            
            
        
