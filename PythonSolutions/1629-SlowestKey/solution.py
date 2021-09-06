# https://leetcode.com/problems/slowest-key/



class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        if len(keysPressed) == 0:
            return keysPressed[0]
        
        diff = 0
        max_diff = releaseTimes[0]
        slow_key = keysPressed[0]
        
        i = 1
        
        while i < len(keysPressed):
            diff = releaseTimes[i] - releaseTimes[i - 1]
            if diff > max_diff:
                max_diff = diff
                slow_key = keysPressed[i]
            elif diff == max_diff:
                if ord(keysPressed[i]) > ord(slow_key):
                    slow_key = keysPressed[i]
            i += 1
        
        return slow_key
        
        
