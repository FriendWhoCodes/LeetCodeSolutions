# https://leetcode.com/problems/univalued-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        value = root.val
        
        if root.left:
            if root.left.val != value:
                return False
        if root.right:
            if root.right.val != value:
                return False
        
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
                
        
        
