

# Bruteforce solution
# Time:  O(n^2), Space: O(1)
# 52 / 58 test cases pass on LC

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] == nums[j] and i != j:
                    return nums[i]
