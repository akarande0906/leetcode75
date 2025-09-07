'''
LC 101: Symmetric Tree
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
                      1
                    /    \
                   2      2
                  / \    / \
                 3   4  4   3
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
    ''' Iterative Solution'''
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append((root.left, root.right))
        while queue:
            left, right = queue.popleft()
            if left and right and left.val == right.val:
                queue.append((left.left, right.right))
                queue.append((left.right, right.left))
            elif left or right:
                return False
        return True

    ''' Recursive Solution '''
    def isSymmetricRecursive(self, root: Optional[TreeNode]) -> bool:
        def checkSymmetry(left, right):
            if not left and not right:
                return True
            if left and right:
                if left.val != right.val:
                    return False
                else:
                    return checkSymmetry(left.left, right.right) and checkSymmetry(left.right, right.left)

            return False
        return checkSymmetry(root.left, root.right)
    
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


sol = Solution()
print(sol.isSymmetric(_create_tree([1,2,2,3,4,4,3])))
print(sol.isSymmetric(_create_tree([1,2,2,None,3,None,3])))



