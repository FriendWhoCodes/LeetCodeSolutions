'''
1. Brute Force Approach: Run two loops and try with all possibilites. Except the cases where the number is repeated 
(e.g. in [1,5,5], answer is [1,2] and not [1,1] or [2,2]. Same index is not allowed.)

Runtime: 7736 ms, faster than 5.00% of Python3 online submissions for Two Sum.
Memory Usage: 14.9 MB, less than 39.53% of Python3 online submissions for Two Sum.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = []
        length = len(nums)
                
        for i in range(0, length):
            for j in range(1, length):
                if (target - nums[i] == nums[j] and i != j):
                    solution.append(i)
                    solution.append(j)
                    return solution
            
        return solution
                
            
        
        
        
