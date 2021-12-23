# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

# Sort the array and calculate the difference between the first two numbers.
# Then use two pointers in a loop to check if the consecutive numbers have the same difference. If not return False and exit the loop else return True at the end.

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        
        diff = arr[1] - arr[0]
        n = len(arr)
        
        i, j = 0, 1
        
        while i < n and j < n:
            if arr[j] - arr[i] != diff:
                return False
            i += 1
            j += 1
        
        return True
