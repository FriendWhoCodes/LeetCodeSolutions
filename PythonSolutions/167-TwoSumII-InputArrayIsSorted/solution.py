# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# TODO
# Using Binary Search, an O(n) solution:



# Using Two Pointers, O(n)

# We initialize two pointers to start and end indices
# We get the sum of values for both of these incdices
# If sum == target, we return the indices value
# Otherwise if sum is less than target, we incremenet the left pointer
# Else if sum is higher than target, we decrement the right pointer
# Since at some point the targets would meet if the solution is there, the worst csae complexity is O(n)

# This works, since the input array is sorted, the sum would be less towards the left of the array
# And highest towards the right
# So with this we can navigate the input by comparing the sum with target and tweaking the pointers

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            total = nums[left] + nums[right]
            
            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1
        
        return [-1, -1]
        
       

# Using hash table, though test cases pass in LC, does not take advantage of the fact that the array is sorted:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        freq = {}
        
        for i in range(len(nums)):
            freq[nums[i]] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in freq and freq[diff] != i:
                return [i+1, freq[diff] + 1]
        
        return [-1, -1]

# Bruteforce, does not take into account that the array is sorted
# Time Limit Exceeded on LC, 18 / 19 test cases passed.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        diff = 0
        for i in range(len(numbers)):
            diff = target - numbers[i]
            for j in range(1, len(numbers)):
                if numbers[j] == diff and i != j:
                    # Add 1 since the indices are one indexed
                    return [i+1, j+1] 
        return [-1, -1]
                
