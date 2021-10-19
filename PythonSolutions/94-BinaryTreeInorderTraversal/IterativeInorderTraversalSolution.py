
# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return
        
        stack = []
        result = []
        current = root
        
        # Go to the leftmost node and append all left nodes onto the stack
        while current is not None:
            stack.append(current)
            current = current.left
            
        # If there is any element on the stack, pop it and append it to the result array
        while len(stack) > 0:
            current = stack.pop()
            result.append(current.val)
            
            # With left subtree processed, focus on the right subtree
            current = current.right
            while current is not None:
                stack.append(current)
                current = current.left
        
        return result
            
        
