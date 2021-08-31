# https://leetcode.com/problems/container-with-most-water/




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
                
        
