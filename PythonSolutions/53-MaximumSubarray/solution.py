# https://leetcode.com/problems/maximum-subarray


# Kadane's Algorithm, O(n) solution




# Bruteforce Solution
# Time limit exceeded, 202 / 203 test cases passed.

from math import inf
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        max_sum = -inf
        
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total +=  nums[j]
                max_sum = max(total, max_sum)
        return max_sum
