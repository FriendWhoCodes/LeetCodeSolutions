# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
# Difficulty: Medium

# Complexity - Time: O(n) and Space: O(n)

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # 1 << k returns 2 ^ k 
        expected = 1 << k   # or #  expected = 2 ** k
        checked = set()

        n = len(s)

        for i in range(n - k + 1):      # So we can check till the rightmost possible substring
            temp = s[i:i+k]
            if temp not in checked:
                checked.add(temp)
                
                if expected == len(checked):
                    return True
        
        return False
