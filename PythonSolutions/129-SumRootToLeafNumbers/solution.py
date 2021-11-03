# Recursive DFS solution


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:        

        return self.helper(root)
            
        
    def helper(self, node, cur=0):
        if not node: 
            return 0

        # If leaf node, then add to the current value
        if not node.left and not node.right:
            return cur * 10 + node.val
        
        # Calculate the value for the left and right sides
        left = self.helper(node.left, cur*10 + node.val)
        right = self.helper(node.right, cur * 10 + node.val)

        return left + right
        
