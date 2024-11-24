'''
LC 1650: Lowest Common Ancestor of Binary Tree III
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

e.g.
           3
         /   \
        5     1
       / \   /  \
      6  2   0   8
        / \
       7   4   p = 5 and q = 1    => LCA = 3
 '''


# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def find_depth(node):
            depth = 0
            while node:
                depth += 1
                node = node.parent
            return depth
        
        # First find the depth of both nodes p and q
        
        p_depth = find_depth(p)
        q_depth = find_depth(q)

        # If the depths dont match, we match them
        if p_depth != q_depth:
            if p_depth < q_depth:
                while p_depth != q_depth:
                    q = q.parent
                    q_depth -= 1
            elif p_depth > q_depth:
                while p_depth != q_depth:
                    p = p.parent
                    p_depth -= 1
        # Finally once depths are matched, we find the common parent
        while p != q:
            p = p.parent
            q = q.parent
        return p
                



            
                
