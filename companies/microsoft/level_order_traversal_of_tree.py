'''
Leetcode 102: Binary Tree Level ordered traversal
'''
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_array = []
        if not root:
            return []
        queue = deque([root])

        while queue:
            current_level = []
            for _ in len(queue):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_array.append(current_level)
        
        return level_array

            
