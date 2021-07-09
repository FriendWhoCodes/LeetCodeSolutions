# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def height(node):
            if not node:
                return 0
            else:
                return max(height(node.left), height(node.right)) + 1
        
        
        l_height = height(root.left)
        r_height = height(root.right)
        
        
        l_diam = self.diameterOfBinaryTree(root.left)
        r_diam = self.diameterOfBinaryTree(root.right)
        
        return max(l_height + r_height, max(l_diam, r_diam))    
 



    
        
