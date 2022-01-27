# 1305. All Elements in Two Binary Search Trees
# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

# Kind of bruteforce method:
# Do the inorder traversal of both BSTs and get the two lists with the traversals
# Since it's BST and we did in order traversal, the lists would be sorted
# Now ideally these two sorted lists need to be merged but I was failing most likely due to the different lengths and didn't spend more time
# Due to the daily challenge time running out, TODO Fix that
# Otherwise just extend a result list and add the two lists elements to it and sort the sorted list and return it.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        first = []
        second = []
        
        if root1:
            first = self.in_order(root1, first)
        if root2:
            second = self.in_order(root2, second)
        
        result = []
        
        m = len(first)
        n = len(second)
        
        if m > 0:
            result.extend(first)
        if n > 0:
            result.extend(second)
        
        result.sort()
        return result
        
        
    def in_order(self, root, result):
        if root:
            self.in_order(root.left, result)
            result.append(root.val)
            self.in_order(root.right, result)
            
            return result
        
# I Couldn't properly merge these two arrays of different lengths
# TODO fix this without using sort of O(nlogn)
        
#         i = j = 0
#         result = []
#         while i < m and j < n:
#             if first[i] <=second[j]:
#                 result.append(first[i])
#                 i += 1
#                 print("i is: ", i)
#             elif first[i] > second[j]:
#                 result.append(second[j])
#                 j += 1
#                 print("j is: ", j)
        
        
        
        
    
  
        


