'''
Given the root node of a directed graph, clone this graph by creating its deep copy so that the cloned graph has the same vertices and edges as the original graph.
'''

# Definition for a graph node
class Node:
  def __init__(self, d):
    self.data = d
    self.neighbors = []
from collections import deque

def clone(root):
    bst = {}
    q = deque()
    q.append(root)
    new_root = Node(root.data)
    bst[root] = new_root
    while q:
       cur = q.popleft()
       node = bst[cur]
       neighbors = cur.neighbors
       c_neighbors = []
       for n in neighbors:
          if not n in bst:
             q.append(n)
             bst[n] = Node(n.data)
          c_neighbors.append(bst[n])
       node.neighbors = c_neighbors
    return new_root
             
             

  
