# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        
        self.helper(root, result)
        return result
    
    def helper(self, root, temp):
        if root:
            self.helper(root.left, temp)
            temp.append(root.val)
            self.helper(root.right, temp)
        
