'''
LC 501: Find Mode in Binary Search Tree
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.
If the tree has more than one mode, return them in any order.
Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> list[int]:
        self.max_streak = 0
        self.cur_streak = 0
        self.cur_num = 0
        self.ans = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            num = node.val
            if num == self.cur_num:
                self.cur_streak += 1
            else:
                self.cur_streak = 1
                self.cur_num = num
            if self.cur_streak > self.max_streak:
                self.ans = []
                self.max_streak = self.cur_streak
            if self.cur_streak == self.max_streak:
                self.ans.append(num)
            inorder(node.right)
        
        inorder(root)
        return self.ans
def _create_tree(arr):
        if not arr:
            return None
        root = TreeNode(arr[0])
        n = len(arr)
        q = [root]
        i = 1
        while i < n:
            node = q.pop(0)
            if arr[i] is not None:
                node.left = TreeNode(arr[i])
                q.append(node.left)
            i += 1
            if i < n and  arr[i] is not None:
                node.right = TreeNode(arr[i])
                q.append(node.right)
            i += 1
        return root

print (Solution().findMode(_create_tree([1,None,2,2])))
print (Solution().findMode(_create_tree([0])))
