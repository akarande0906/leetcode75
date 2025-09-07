'''
LC 199: Binary Right Side View
E.g.:
         1
       /   \
      2     3
       \     \
       5      4  => Return [1, 3, 4] 
       Note if 4 was missing, return [1, 3, 5]
'''
from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    max_level = 1
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        q = deque()
        q.append(root)
        ret_arr = []
        while q:
            n = len(q)
            add_node = False
            for nodes in range(n):
                node = q.popleft()
                if node:
                    if not add_node:
                        ret_arr.append(node.val)
                        add_node = True
                    if node.right:
                        q.append(node.right)
                    if node.left:
                        q.append(node.left)
        return ret_arr
    
    def rightSideViewDFS(self, root: Optional[TreeNode]) -> list[int]:
        level_map = {}
        ret_arr = []
        def dfs(node, level):
            if not node:
                return
            if not level in level_map:
                level_map[level] = node.val
            self.max_level = max(self.max_level, level)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        dfs(root, 1)
        if level_map:
            for lev in range(1, self.max_level + 1):
                ret_arr.append(level_map[lev])
        return ret_arr
    
    def _create_tree(self, arr):
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
            if arr[i] is not None and i < n:
                node.right = TreeNode(arr[i])
                q.append(node.right)
            i += 1
        return root
    

sol = Solution()
print (sol.rightSideView(sol._create_tree([1,2,3,None,5,None,4])))
print (sol.rightSideViewDFS(sol._create_tree([1,2,3,None,5,None,4])))
print (sol.rightSideView(sol._create_tree([1,2,3,None,5,None,4,6,None])))
print (sol.rightSideViewDFS(sol._create_tree([1,2,3,None,5,None,4,6,None])))
            
