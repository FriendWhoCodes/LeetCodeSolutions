# https://leetcode.com/problems/defanging-an-ip-address/


class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = ""
        
        for char in address:
            if char != ".":
                result += char
            else:
                result += "[.]"
        
        return result
                
        

