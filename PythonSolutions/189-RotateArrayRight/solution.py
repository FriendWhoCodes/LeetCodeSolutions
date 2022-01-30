# https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k < 0 or k is None:
            return
        
        k = k % len(nums)
        # First revese whole array
        # Then reverse k part
        # Then reverse (n-k) part
        
        def reverse (start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
    
        reverse(0, n-1)
        print(nums)
        reverse(0, k-1)
        print(nums)
        reverse(k, n - 1)
        print(nums)
        
       
    
        # Alternate solution
        # O(n*k) time and O(1) space complexity
        
        '''
        class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k:
            nums = self.right_rotate(nums)
            k -= 1
        # print(nums)
    
    def right_rotate(self, arr):
        n = len(arr)
        temp = arr[n-1]
        
        for i in range(n-2,-1,-1):
            arr[i+1] = arr[i]
        # print(arr)
        
        arr[0] = temp
        
        return arr
        '''
        
        
        # Rotates the array to the right:
        # O(n*k) time and O(1) space complexity
        # Time Limit Exceeded
        '''
        for _ in range(k):
            last = nums[-1]
            for i in range(n -1, -1, -1):       
                nums[i] = nums[i - 1]
            nums[0] = last
            
        '''
        
        
        # Rotates the array to the left:
        # O(n*k) time and O(1) space complexity
        # Time Limit Exceeded
        '''
        n = len(nums)
        
        for _ in range(k):
            temp = nums[0]
            for i in range(length):
                nums[i] = nums[i+1]
            nums[length - 1] = temp
        '''
