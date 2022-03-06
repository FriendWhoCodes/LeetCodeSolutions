# https://leetcode.com/problems/richest-customer-wealth/
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        max_wealth = 0
        
        for wealth in accounts:
            total = sum(wealth)
            max_wealth = max(total, max_wealth)
        
        return max_wealth
            
'''
# In latest attempt:

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        cur_wealth = 0
        max_wealth = 0
        
        for account in accounts:
            cur_wealth = sum(account)
            max_wealth = max(cur_wealth, max_wealth)
        
        return max_wealth
        

'''
                
                
        
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
