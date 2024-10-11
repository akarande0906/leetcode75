'''
Given a Binary Tree, figure out whether it’s a Binary Search Tree. In a binary search tree, each node’s key value is smaller than the key value of all nodes in the right subtree, and is greater than the key values of all nodes in the left subtree.
'''

# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

def is_bst_rec(root, minVal, maxVal):
  if root is None:
     return True
  if not (minVal < root.data < maxVal):
     return False
  return is_bst_rec(root.left, minVal, root.data) and is_bst_rec(root.right, root.data, maxVal)

def is_bst(root):
    return is_bst_rec(root, float('-inf'), float('inf'))
