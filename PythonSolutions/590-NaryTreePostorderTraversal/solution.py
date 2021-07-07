"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        
        self.helper(root, result)
        
        return result
    
    
    def helper(self, root, temp):
        if root:
            for node in root.children:
                self.helper(node, temp)
            temp.append(root.val)
