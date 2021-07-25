# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        result = []
        result.append(self.first_occurrence(nums, target))
        result.append(self.last_occurrence(nums, target))
        return result
    
    def first_occurrence(self, nums, target):
        low = mid = 0 
        high = len(nums) - 1
        first = -1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if target == nums[mid]:
                first = mid
                high = mid - 1
            elif target < nums[mid]:
                    high = mid - 1
            else:
                low = mid + 1
        return first
    
    def last_occurrence(self, nums, target):
        low = mid = 0 
        high = len(nums) - 1
        last = -1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if target == nums[mid]:
                last = mid
                low = mid + 1
            elif target < nums[mid]:
                    high = mid - 1
            else:
                low = mid + 1
        return last
            
            
