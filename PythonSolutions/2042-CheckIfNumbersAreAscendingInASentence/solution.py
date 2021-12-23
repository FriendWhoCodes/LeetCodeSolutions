

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        temp = s.split()
        result = []
        
        for item in temp:
            if item.isnumeric():
                result.append(item)
                
        i, j = 0, 1
        n = len(result)
        print(result)
        
        while i < n and j < n:
            if int(result[i]) >= int(result[j]):
                return False
            i += 1
            j += 1
        
        return True
        
