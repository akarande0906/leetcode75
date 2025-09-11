'''
Leetcode 133: Clone Graph
'''
from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    # This is an undirected connected graph and when we start at one node
    # we will eventually traverse all nodes and edges
    # For each node, we create a new 'cloned' node. 
    # Map the node to the cloned node.
    # Now for each neighbor of the original node, call clone on the neighbor.
    # If the node was seen before, we just return the node.
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone_map = {}

        def clone(node: Optional['Node']) -> Optional['Node']:
            if node in clone_map:
                return clone_map[node]
            cloned_node = Node(node.val, [])
            clone_map[node] = cloned_node
            for n in node.neighbors:
                cloned_node.neighbors.append(clone(n))
            return cloned_node
        
        return clone(node) if node else None


