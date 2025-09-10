'''
Leetcode 110: Balanced Binary Tree
'''
from typing import List, Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def _create_tree(self, arr : Optional[List[int]]) -> TreeNode:
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
            if i < n and arr[i] is not None:
                node.right = TreeNode(arr[i])
                q.append(node.right)
            i += 1
        return root
    

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def isBalancedHelper(root: TreeNode) -> Tuple[bool, int]:
            if not root:
                return True, -1 # Terminating condition
            
            # Check left subtree
            left_balanced, left_height = isBalancedHelper(root.left)
            if not left_balanced:
                return False, 0
            right_balanced, right_height = isBalancedHelper(root.right)
            if not right_balanced:
                return False, 0
            
            return (abs(left_height - right_height) < 2), \
                1 + max(left_height, right_height)
        
        return isBalancedHelper(root)[0]