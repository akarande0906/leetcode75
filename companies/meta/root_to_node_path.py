'''
LC 129: Sum Root to Leaf Numbers:
          4
        /   \
       9     0
      / \    
     5   1     => 495 + 491 + 40 = 1026
'''

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        totalSum = 0
        def dfs(node, sumNumbers):
            nonlocal totalSum
            if not node:
                return
            sumNumbers = sumNumbers * 10 + node.val
            if not node.left and not node.right:
                totalSum += sumNumbers
                return
            dfs(node.left, sumNumbers)
            dfs(node.right, sumNumbers)
        dfs(root, 0)
        return totalSum
    
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
print (sol.sumNumbers(sol._create_tree([4,9,0,5,1])))
print (sol.sumNumbers(sol._create_tree([1,2,3])))
print (sol.sumNumbers(sol._create_tree([1,2,3,4,5,6,7])))