'''
LC 1372: Longest ZigZag Path in a Binary Tree
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        max_len = 0
        def zigzag(node, goLeft, length):
            nonlocal max_len
            if not node: 
                return
            max_len = max(max_len, length)
            if goLeft:
                zigzag(node.right, True, 1)
                zigzag(node.left, False, length + 1)
            else:
                zigzag(node.left, False, 1)
                zigzag(node.right, True, length + 1)
        zigzag(root, True, 0)
        return max_len
    
longestZigZag = Solution().longestZigZag
print(longestZigZag(_create_tree([1,1,1,None,1,None,None,1,1])))
print(longestZigZag(_create_tree([1,1,1,None,1,None,None,None,1])))
print(longestZigZag(_create_tree([1,1,1,None,1,None,None,None,1])))
print(longestZigZag(_create_tree([1,None,1,1,1,None,None,1,1,None,1,None,None,None,1])))

        