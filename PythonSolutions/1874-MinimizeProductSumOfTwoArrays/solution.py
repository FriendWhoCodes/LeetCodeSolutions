# https://leetcode.com/problems/minimize-product-sum-of-two-arrays/

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        sum = 0
        
        nums1.sort()
        nums2.sort(reverse=True)
        
        for i in range(n):
            sum += nums1[i] * nums2[i]
        
        print(sum)
        return sum
            
