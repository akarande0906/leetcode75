# Definition for a binary tree node.
from typing import Optional
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        else:
            temp = root.left
            root.left = root.right
            root.right = temp
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root

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
      if arr[i] is not None and i < n:
          node.right = TreeNode(arr[i])
          q.append(node.right)
      i += 1
   return root



arr = [4,2,7,1,3,6,9]
root = _create_tree(arr)
root = Solution().invertTree(root)        

