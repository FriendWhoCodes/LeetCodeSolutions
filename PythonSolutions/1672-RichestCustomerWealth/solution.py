# https://leetcode.com/problems/richest-customer-wealth/
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        max_sum = 0
        for row in accounts:
            max_sum = max(sum(row), max_sum)
        
        return max_sum
            
        
                
                
        
'''
        Example :
        
         j =  1, 2, 3
        i = 1 [1,2,3],
            2 [3,2,1]
        
        accounts[1][1] = 1
        accounts[1][2] = 2
        accounts[1][3] = 3
        sum = 6
        
        accounts[2][1] = 3
        accounts[2][2] = 2
        accounts[2][3] = 1
        sum = 6
        
        max_wealth = max(6,6) here, = 6
'''
