# https://leetcode.com/problems/container-with-most-water/




# Bruteforce solution, Time Limit Exceeded
# Passes only 49/60 test cases on LC
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
                
                if area > max_area:
                    max_area = h*w
        return max_area
                
        
