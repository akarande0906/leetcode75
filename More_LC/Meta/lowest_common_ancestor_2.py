'''
LC 236: Lowest Common ancestor of Binary Tree without parent pointer
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        # Create a parent map
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        # Now both p and q are found
        # Mark all ancestors of p
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        # Find if a parent of q is in ancestor set of p
        while q not in ancestors:
            q = parent[q]
            
        return q
        