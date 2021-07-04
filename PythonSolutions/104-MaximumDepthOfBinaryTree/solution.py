# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
    
        depth1 = self.maxDepth(root.left)
        depth2 = self.maxDepth(root.right)
        
        return max(depth1, depth2) + 1    
        
