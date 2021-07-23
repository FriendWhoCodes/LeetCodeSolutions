# 1470. Shuffle the Array
# https://leetcode.com/problems/shuffle-the-array/


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        
        i = 0
        j = n
        while(i < j and j < 2*n):
            result.append(nums[i])
            result.append(nums[j])
            i += 1
            j += 1
                
        return result
            
            
        
        
