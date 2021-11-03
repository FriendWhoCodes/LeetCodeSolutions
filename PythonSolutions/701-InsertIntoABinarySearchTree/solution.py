# https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        
        # Since all the values are unique, if the key is already present, then no need to insert
        elif val == root.val:
            return root
        
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        
        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        
        return root
        
        
        
