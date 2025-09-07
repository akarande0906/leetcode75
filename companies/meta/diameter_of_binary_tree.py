'''
LC 543: Diameter of Binary Tree
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Note: Max path will always end at a leaf node
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def findLongestPath(node):
            nonlocal diameter
            if not node:
                return 0
            left_dist = findLongestPath(node.left)
            right_dist = findLongestPath(node.right)
            diameter = max(diameter, left_dist + right_dist)
        
            return max(left_dist, right_dist) + 1
        findLongestPath(root)
        return diameter
    