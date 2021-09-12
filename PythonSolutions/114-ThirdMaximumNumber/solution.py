# Question: Return the third maximum element in the array if it exists, else return the maximum element in the array


# O(nlogn) solution

# First uses reverse sorting to reverse sort the array
# Then uses a seen array to remove possible duplicates and only store unique elements
# Then if the array length is 3 or more, returns the third element
# Else returns the first element of seen.


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        nums.sort(reverse = True) # o(nlogn)
        
        seen = []                 # For getting unique elements
        
        for num in nums:
            if num not in seen:
                seen.append(num)
                
        if len(seen) >= 3:
            return seen[2]
        else:
            return seen[0]
            
            
            
        
        
            
            
            
        
