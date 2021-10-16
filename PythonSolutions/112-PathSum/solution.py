# https://leetcode.com/problems/path-sum/

# Complexity: Time: O(n) and Space: O(h) complexity

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root is None:
            return 
        
        # Reduce root's value from the total
        targetSum -= root.val
        
        # if left and right nodes are None and target sum has reduced to 0, then return True
        if root.left is None and root.right is None:
            if targetSum == 0:
                return True
        
        # Else apply the same logic on left or right subtree, if any of them are true
        # Then we found the path sum and can exit the method
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
        
        
