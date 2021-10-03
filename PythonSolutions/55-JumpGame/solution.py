

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        length = len(nums)
        last_pos = length - 1
        
        max_reach_index = 0
        for i in range(length):
            if i + nums[i] >= max_reach_index:
                max_reach_index = i + nums[i]
            if i == max_reach_index:
                break
                
        if max_reach_index >= last_pos:
            return True
        
        
        
