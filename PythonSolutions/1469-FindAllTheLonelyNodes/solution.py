# https://leetcode.com/problems/find-all-the-lonely-nodes/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        
        result = []
        
        self.helper(root, result)
        
        return result
        
        
        
    def helper(self, root, result):
        if root:
            if root.left and root.right is None:
                result.append(root.left.val)
        
            elif root.right and root.left is None:
                result.append(root.right.val)
                
            self.helper(root.left, result)
            self.helper(root.right, result)
        
        
            
        
