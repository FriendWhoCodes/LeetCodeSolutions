# https://leetcode.com/problems/largest-number-at-least-twice-of-others/
# Difficulty: Easy

# Complexity: Time: O(n) and Space: O(1)

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = -math.inf
        large_i = 0
        
        for i, num in enumerate(nums):
            if num > largest:
                largest = num
                large_i = i

        for i in range(len(nums)):
            if i != large_i and nums[i] * 2 > largest:
                return -1
        
        return large_i
        
        
