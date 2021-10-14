# https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # Sets don't work because the repeated elements are removed and ans requires it
#         set1 = set(nums1)
#         set2 = set(nums2)
        
#         result = []
        
#         result = set1.intersection(set2)
#         return result
    
    # Through hash table
    
        freq1 = {}
        result = []
        
        for num in nums1:
            if num not in freq1:
                freq1[num] = 1
            else:
                freq1[num] += 1
                
        freq2 = {}        
        for num in nums2:
            if num not in freq2:
                freq2[num] = 1
            else:
                freq2[num] += 1
        
        smaller_dic = None
        
        if len(freq1) <= len(freq2):
            smaller_dic = freq1
        else:
            smaller_dic = freq2
        
        for key, value in smaller_dic.items():
            if key in freq1 and key in freq2:
                count = min(freq1[key], freq2[key])
                while count > 0:
                    result.append(key)
                    count -= 1
        
        return result
        
