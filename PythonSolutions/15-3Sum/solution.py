# https://leetcode.com/problems/3sum/

# Two pointers solution:
# First we sort the function, so we can apply the two sum logic here
# We create a separate function from two sum
# We call that function for each value of the nums array and calculate the sum with this value and the two pointers


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i == 0 or nums[i] != nums[i - 1]:
                self.two_pointers_sum(nums, i, result)
        
        return result
    
    
    def two_pointers_sum(self, nums, i, result):
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([ nums[i], nums[left], nums[right] ])
                left += 1
                right -= 1
                
                while nums[left] == nums[left - 1] and left < right:
                    left += 1




# O(n^3logn) solution, my worst LC Solution but still passed 315/318 test cases 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        result = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0 and i != j != k:
                        temp = [nums[i], nums[j], nums[k]]
                        temp.sort()
                        if temp not in result:
                            result.append(temp)
                            print(i, j, k)
        
        return [list(i) for i in set(tuple(i) for i in result)]
        
