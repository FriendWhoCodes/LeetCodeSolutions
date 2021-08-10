# https://leetcode.com/problems/build-array-from-permutation/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = []
        
        for i in nums:
            result.append(nums[i])
        
        return result
      
# TODO - Do it in constant space
        
