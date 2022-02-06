# In place solution using two pointers
# Time Complexity: O(n) and Space: O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        n = len(nums)
        # Set unique index to 1 since the first element is always unique among the elements we've seen so far
        unique_i = 1 
        
        # (n - 1) so that we don't go out of index when we compare second last and last elements
        for i in range(n - 1):
            if nums[i] != nums[i+1]:
                nums[unique_i] = nums[i + 1]    # No need to swap, just replace
                unique_i += 1
        
        return unique_i
