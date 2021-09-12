




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
        
