# This implements Binary Tree and some common methods in Python

# Create the node structure class:

import math

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    
    # Do different Trversals:
    # Preorder, Time: O(n), Space: O(h)
  def pre_order(self, root):
    if root is not None:
      print(root.val)
      self.pre_order(root.left)
      self.pre_order(root.right)
    
    # Inorder, Time: O(n), Space: O(h)
  def in_order(self, root):
    if root is not None:
      self.in_order(root.left)
      print(root.val)
      self.in_order(root.right)

    # Postorder, Time: O(n), Space: O(h)
  def post_order(self, root):
    if root is not None:
      self.post_order(root.left)
      self.post_order(root.right)
      print(root.val)

    # Count of nodes in Binary Tree, Time: O(n), Space: O(h)
  def count(self, root):
    if root is None:
        return 0
    else:
        return self.count(root.left) + self.count(root.right) + 1

    # Maximum value of any node in a Binary Tree, Time: O(n), Space: O(h)
  def max(self, root):
    if root is None:
        return -inf
    else:
        return max(root.val, self.max(root.left), self.max(root.right))
    
    # Search for a key in Binary Tree, trturn True if there, False otherwise
    # Time: O(n), Space: O(h)
  def search(self, root, key):
    if root is None:
        return False
    else:
        if root.val == key:
            return True
        else:
            if self.search(root.left, key):
                return True
            else:
                return self.search(root.right, key)
            # The below code is slightly less efficient? Since we check both branches of the root here
            # return self.search(root.left, key) or self.search(root.right, key)

# Driver Code

# Create the tree: 

tree = Node(2)
tree.left = Node(4)
tree.right = Node(6)
tree.left.left = Node(8)
tree.left.right = Node(10)
tree.right.left = Node(12)
tree.right.right = Node(15)

print("Preorder Traversal")        
tree.pre_order(tree)

# print("Inorder Traversal")        
# tree.in_order(tree)

# print("Postorder Traversal")        
# tree.post_order(tree)

print("Count of the binary tree is: ", tree.count(tree))

print("Maximum of the binary tree is: ", tree.max(tree))

print("Is 12 present in binary tree is: ", tree.search(tree, 12))
print("Is 5 present in binary tree is: ", tree.search(tree, 5))
print("Is A present in binary tree is: ", tree.search(tree, "A"))
print("Is 2 present in binary tree is: ", tree.search(tree, 2))


      
      
