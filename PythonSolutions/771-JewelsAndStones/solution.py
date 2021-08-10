# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = {}
        
        for jewel in jewels:
            freq[jewel] = 0
        
        for stone in stones:
            if stone in freq:
                freq[stone] += 1
        
        return (sum(list(freq.values())))
        
        
        
# Bruteforce solution
        
# class Solution:
#     def numJewelsInStones(self, jewels: str, stones: str) -> int:        
#         count = 0
#         for jewel in jewels:
#             for stone in stones:
#                 if jewel == stone:
#                     count += 1
#         return count
        
        
        
