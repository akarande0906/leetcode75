class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right    

class Solution:
    def lca(self, root: TreeNode, nodes: list[TreeNode]) -> TreeNode:
        node_set = set(nodes)
        def helper(root):
            if root is None:
                return None
            if root.val in node_set:
                return root

            left = lca(root.left)
            right = lca(root.right)

            if left and right:
                return root
            return left if left else right
        return helper(root)
