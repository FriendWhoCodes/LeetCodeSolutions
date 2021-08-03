# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        
        total = 0
        if root is None:
            return 0
        
        if root:
            if root.val <= high and root.val >= low:
                total += root.val
        if root.left:
            total =  total + self.rangeSumBST(root.left, low, high) 
        
        if root.right:
            total = total + self.rangeSumBST(root.right, low, high)
            
        return total
            
        
