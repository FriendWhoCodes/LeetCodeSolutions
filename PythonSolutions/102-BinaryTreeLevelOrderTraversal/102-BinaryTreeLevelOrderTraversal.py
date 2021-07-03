# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        queue = deque()
        result = []
        
        queue.append(root)
        
        while(queue):
            current_level = []
            
            for i in range(len(queue)):
                temp = queue.popleft()
                if temp.left:
                    queue.append(temp.left)
                
                if temp.right:
                    queue.append(temp.right)
                
                current_level.append(temp.val)
            result.append(current_level)
        return result
                
            
        
