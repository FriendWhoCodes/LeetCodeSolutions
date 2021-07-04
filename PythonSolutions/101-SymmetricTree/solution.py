# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        return self.is_mirror_image(root.left, root.right)
    
    
    def is_mirror_image(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        
        if root1 and root2:
            if root1.val == root2.val:
                return self.is_mirror_image(root1.left, root2.right) and self.is_mirror_image(root1.right, root2.left)
        
        return False
            
        
