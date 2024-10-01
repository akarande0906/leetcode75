# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, float('-inf'), float('inf'))]
        while len(stack)>0:
            current, low, high = stack.pop()
            if not (low < current.val < high): return False # whenever we find any node not following the order, then we directly return False
            if current.left: stack.append((current.left, low, current.val))
            if current.right: stack.append((current.right, current.val, high))
        return True


