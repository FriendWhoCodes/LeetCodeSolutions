# https://leetcode.com/problems/container-with-most-water/

# The water area is the area of rectabgle, given by height * width here
# But height is the limiting factor here, since the water level is limited to the lower heights, as otherwise water will spill
# So we get max area as: min(height[i], height[j]) * (j - i)

# O(1) solution:
# Use two pointers and start with the max width. i.e. i=0 and j = len(height) - 1
# Calculate the area and keep comparing it to the max_area so far.
# If you get any lower height, at any of the pointer indices, move that pointer to left or right appropriately.


# Why we move the pointer with the lower height value?
# Because the lower height value would not support a higher water level, so we can remove it.
# Since we start with max width, we need to optimize on height and we keep on ignoring the lower height values


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        if n <=1:
            return 0
        
        max_area = 0
        i, j = 0, n - 1
        
        while i < j:
            h = min(height[i], height[j])
            w = j - i
                
            area = h * w
            max_area = max(area, max_area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
                   
        return max_area
                
        



# Bruteforce solution, Time Limit Exceeded
# Passes only 49/60 test cases on LC
# Time Complexity = O(n^2) and Space: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        if n <=1:
            return 0
        
        max_area = -1
        for i in range(n):
            for j in range(i+1, n):
                h = min(height[i], height[j])
                w = j - i
                
                area = h * w
                max_area = max(area, max_area)
                
        return max_area
                
        
