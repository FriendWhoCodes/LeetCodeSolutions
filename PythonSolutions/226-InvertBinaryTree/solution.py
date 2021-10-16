# https://leetcode.com/problems/invert-binary-tree/

# Recursive solution
# O(n) time complexity, O(h) space complexity - where h = height of the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        
        return root
        

# Recursive solution
# O(n) time complexity, O(n) space complexity
