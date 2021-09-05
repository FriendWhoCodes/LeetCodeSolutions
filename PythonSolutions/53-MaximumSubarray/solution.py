# https://leetcode.com/problems/maximum-subarray


# Kadane's Algorithm, O(n) solution

# Optimized Solution using Kadane's Algorithm
# Here we keep the subarray's sum in case when the sum is positive
# If not we make the sum as zero and keep going


from math import inf
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
  
    # current_subarray keeps the sum of the current subarray
    # max_subarray keeps the sum of max of all subarray sums
        current_subarray = max_subarray = nums[0]
    
    # We iterate through the aray from second element i.e. index 1
    # We add the sum of values of each element to the current_subarray
    # If current_subarray becomes negative, then we 
        
        for i in range(1, len(nums)):
        # Add current element to current_subarray if the sum is more than current element
        # Else just take the current element (max takes care of this check)
            current_subarray = max(nums[i], current_subarray + nums[i])
        # To keep a track of max_subarray so far,
        # Update the max of current_subarray and max_subarray in the max_subarray
            max_subarray = max(max_subarray, current_subarray)
        
        return max_subarray


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
