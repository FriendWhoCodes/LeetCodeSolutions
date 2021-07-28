# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        if root.left is None and root.right is None:
            return True
        
        if root.left:
            if root.left.val >= root.val or self.max_val(root.left) >= root.val:
                return False
        if root.right:
            if root.right.val <= root.val or self.min_val(root.right) <= root.val:
                return False
        
        return self.isValidBST(root.left) and self.isValidBST(root.right)

    
    def max_val(self, root):
        if root is None:
            return  float('-inf')
        
        maximum = root.val
        
        left_max = self.max_val(root.left)
        right_max = self.max_val(root.right)
        
        return max(maximum, left_max, right_max)
    
        
    def min_val(self, root):
        if root is None:
            return  float('inf')
        
        minimum = root.val
        
        left_min = self.min_val(root.left)
        right_main = self.min_val(root.right)
        
        return min(minimum, left_min, right_main)
            
        
        
            
                
