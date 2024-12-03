'''
LC 1644: Lowest Common Ancestor of Binary Tree II
Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes, p and q. 
If either node p or q does not exist in the tree, return null. All values of the nodes in the tree are unique.
According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a binary tree 
T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)". 
A descendant of a node x is a node y that is on the path from node x to some leaf node.
             3
          /     \
         /        \
        5          1
      /   \       /  \
      6    2     0    8      => p, q = 5, 1    => LCA is 3   
          / \                => p, q = 7, 2    => LCA is 5 
         7   4               => p, q = 7, 10   => LCA is null 
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.nodes_found = False

        def dfs(node):
            # If we reach the leaf
            if not node:
                return None
            # Iterate to the left and the right
            left, right = dfs(node.left), dfs(node.right)
            conditions = 0
            # Check if the node matches the target node
            if node in (p, q):
                conditions += 1
            if left:
                conditions += 1
            if right:
                conditions += 1
            # We check for 2 conditions to match because either:
            # At this point we want the two nodes to be found either
            # in the left and right subtree or the node itself and the left or right subtrees
            if conditions == 2:
                self.nodes_found = True
            # We return node if both children were found below it
            # or we found one of the children in the left or right subtree
            if (left and right) or node in (p,q):
                return node
            return left or right

        ans = dfs(root)
        return ans if self.nodes_found else None
    
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
print (sol.lowestCommonAncestor(_create_tree([3,5,1,6,2,0,8,None,None,7,4]), 5, 1))
print (sol.lowestCommonAncestor(_create_tree([3,5,1,6,2,0,8,None,None,7,4]), 5, 4))
print (sol.lowestCommonAncestor(_create_tree([3,5,1,6,2,0,8,None,None,7,4]), 5, 10))
    
