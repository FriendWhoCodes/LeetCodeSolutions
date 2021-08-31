

# Bruteforce Solution with two loops
# Time: O(n^2) and Space: O(1)

# Fails with Time Limit Exceeded Error, 49/60 test case pass.

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
                
        


# Optimized Solution
# Time: O(n) and Space: O(1)

class Solution:
    def trap(self, heights: List[int]) -> int:
        n = len(heights)
        
        if n <= 1:
            return 0
        
        total_water = max_left = max_right  = 0
        left, right = 0, n - 1
        
        while left < right:
            if heights[left] <= heights[right]:
                if heights[left] >= max_left:
                    max_left = heights[left]  
                else:
                    total_water += max_left - heights[left]        # OR max_left - height[left]  
                left += 1 
                    
            else:
                if heights[right] >= max_right:
                    max_right = heights[right]
                else:
                    total_water +=  max_right - heights[right]        # OR max_right - height[left]  
                right -= 1
            
        return total_water
        
        
        
        
