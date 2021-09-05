# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


# Bruteforce, does not take into account that the array is sorted
# Time Limit Exceeded on LC, 18 / 19 test cases passed.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        diff = 0
        for i in range(len(numbers)):
            diff = target - numbers[i]
            for j in range(1, len(numbers)):
                if numbers[j] == diff and i != j:
                    # Add 1 since the indices are one indexed
                    return [i+1, j+1] 
        return [-1, -1]
                
