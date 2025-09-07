# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(current, minVal, maxVal):            
            if not current:
                return True
            if current.val <= minVal or current.val >= maxVal:
                return False
            return dfs(current.left, minVal, current.val) and dfs(current.right, current.val, maxVal)
        
        
        return dfs(root, float('-inf'), float('inf'))
