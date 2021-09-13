# https://leetcode.com/problems/count-primes/


# Sieve of Eratosthenes: O(nloglogn) time complexity and O(n) space complexity
# We mark the numbers which are multiples of a number as non primes and don't divide by them

class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n <= 2:
            return 0
        
        
        nums = {}
        
        for i in range(2, int(n**0.5) + 1):           # from 2 to square root of n
            if i not in nums:
                for multiple in range(i*i, n, i):     # Need to understand this loop better
                    nums[multiple] = 1
        print(nums)
        print(len(nums))
        
        # Out of n numbers, len(nums) would give count of all numbers that are multiple of some number
        # So we remove that count from n to get remaining numbers, which must be primes
        # We also remove two for 1 and n itself, finally we return
        return n - len(nums) - 2
        
        







# Following is a O(n^1.5) solution and it fails with TLE for 2 test cases

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        primes = 0
        
        for i in range(2, n):
            if self.is_prime(i) == True:
                primes += 1
        
        return primes
    
    
    def is_prime(self, n):
        # checked = {}
        print("Checking for: ", n)
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
            # if i not in checked:
            #     checked[i] == True
                
        print("Yes, it's a prime!")
        return True
                
        
        
