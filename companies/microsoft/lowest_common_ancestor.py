'''
Leetcode 236: Lowest Common Ancestor of Binary Tree
'''
from collections import deque
from typing import List, Optional, Tuple

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def _create_tree(self, arr : Optional[List[int]], p: int, q: int) -> Tuple[TreeNode, TreeNode, TreeNode]:
        
        p_node, q_node = None, None

        def _assign_p_or_q_node(node):
            nonlocal p_node, q_node
            if node.val == p:
                p_node = node
            elif node.val == q:
                q_node = node
    

        if not arr:
            return None
        root = TreeNode(arr[0])
        _assign_p_or_q_node(root)
        n = len(arr)
        queue = [root]
        i = 1

        while i < n:
            node = queue.pop(0)
            if i < n and arr[i] is not None:
                node.left = TreeNode(arr[i])
                _assign_p_or_q_node(node.left)
                queue.append(node.left)
            i += 1
            if i < n and arr[i] is not None:
                node.right = TreeNode(arr[i])
                _assign_p_or_q_node(node.right)
                queue.append(node.right)
            i += 1
        return root, p_node, q_node

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        queue = deque([root])
        parent_map = {root: None}
        # Lets iterate over all the nodes of the tree till we find p and q
        while p not in parent_map or q not in parent_map:
            node = queue.popleft()
            if node.left:
                parent_map[node.left] = node
                queue.append(node.left)
            if node.right:
                parent_map[node.right] = node
                queue.append(node.right)
        
        # Now iterate over parent map to add all ancestors of p to a set
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent_map[p]

        # Now we can do the iteration with q, but this time we find the first ancestor of p thats also an ancestor of q
        while q not in ancestors:
            q = parent_map[q]
        return q
    
sol = Solution()
tree, p_node, q_node = sol._create_tree([3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 1)
print(sol.lowestCommonAncestor(tree, p_node, q_node).val)
tree, p_node, q_node = sol._create_tree([3,5,1,6,2,0,8,None,None,7,4], 5, 4)
print(sol.lowestCommonAncestor(tree, p_node, q_node).val)

   