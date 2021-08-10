class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        product = 1
        
        while n > 0:
            temp = n % 10
            sum += temp
            product *= temp
            n = n // 10
        
        return product - sum
            
        
