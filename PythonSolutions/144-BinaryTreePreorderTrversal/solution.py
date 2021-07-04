# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        
        self.helper(root, result)
        
        return result
    
    def helper(self, root, temp):
        if root:
            temp.append(root.val)
            self.helper(root.left, temp)
            self.helper(root.right, temp)
        
        
