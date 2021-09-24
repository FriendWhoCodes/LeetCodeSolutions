# https://leetcode.com/problems/n-th-tribonacci-number/


# Dynamic Programming, I looked at solution here. Need to come up by myself.

class TriSeries:
    def __init__(self):
        n = 38
        self.nums = [0]*n
        
        self.nums[1] = self.nums[2] = 1
        
        for i in range(3, n):
            self.nums[i] = self.nums[i -1] + self.nums[i -2] + self.nums[i -3]

            
            
class Solution:
    tri_series_obj = TriSeries()
    
    def tribonacci(self, n: int) -> int:
        return self.tri_series_obj.nums[n]
