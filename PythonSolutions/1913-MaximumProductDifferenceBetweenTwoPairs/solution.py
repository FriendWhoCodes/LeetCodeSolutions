# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        
        nums.sort()
        
        length = len(nums) - 1
        min1 = nums[0]
        min2 = nums[1]
        max1 = nums[length]
        max2 = nums[length -1]
        
        return ((max1 * max2) - (min1 * min2))
