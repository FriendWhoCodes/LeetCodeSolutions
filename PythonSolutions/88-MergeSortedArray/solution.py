# https://leetcode.com/problems/merge-sorted-array/

# Kind of Bruteforce:
# Take elements from nums2 and add them to the end of nums1, replacing all zeroes.
# This is possible since we are already given m and n that is actual number of elements in nums1


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        for i in range(0,n):
            nums1[m + i] = nums2[i]
        
        nums1.sort()
        
        
                
                
                
        

