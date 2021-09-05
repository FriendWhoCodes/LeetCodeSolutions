# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from math import inf

# Single pass solution
# Keep a track of minimum value and max_profit so far.
# For every element, calculate the difference between that element and minimum of all values so far
# If the difference found is greater than the difference so far, we update the max profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        max_profit = 0
        min_price = inf
        
        for i in range(0, len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
        
        return max_profit
            
        

# Bruteforce Solution
# Time Limit Exceeded 198 / 211 test cases passed.


# Bruteforce Solution, fails on LC 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)
        
        for i in range(0, n):
            profit = 0
            for j in range(i+1, n):
                profit = prices[j] - prices[i]
                max_profit = max(profit, max_profit)
        return max_profit
        
        
