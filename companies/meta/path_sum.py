'''
LC 112: Path Sum: Given the root of a binary tree and an integer targetSum, 
return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, cur_sum):
            if not node:
                return False
            cur_sum += node.val
            if not node.left and not node.right and cur_sum == targetSum:
                return True
            else:
                return dfs(node.left, cur_sum) or dfs(node.right, cur_sum)
        return dfs(root, 0)
    
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
print (sol.hasPathSum(sol._create_tree([5,4,8,11,None,13,4,7,2,None,None,None,1]), 22))
print (sol.hasPathSum(sol._create_tree([1,2,3]), 5))
print (sol.hasPathSum(sol._create_tree([]),0))