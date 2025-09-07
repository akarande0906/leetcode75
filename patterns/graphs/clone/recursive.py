"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloneMap = {}
        def clone(node):
            if node in cloneMap:
                return cloneMap[node]
            clone_node = Node(node.val, [])
            cloneMap[node] = clone_node
            for neighbor in node.neighbors:
                clone_node.neighbors.append(clone(neighbor))
            return clone_node
        return clone(node) if node else None
