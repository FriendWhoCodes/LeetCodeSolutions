# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

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
        
        
