'''
Given the root node of a directed graph, clone this graph by creating its deep copy so that the cloned graph has the same vertices and edges as the original graph.
'''

# Definition for a graph node
# class Node:
#   def __init__(self, d):
#     self.data = d
#     self.neighbors = []

def deep_clone(node, map):
  if not node:
      return None 
  new_node = Node(node.data)
  map[node] = new_node
  for n in node.neighbors:
      if not n in map:
          new_node.neighbors.append(deep_clone(n, map))
      else:
          new_node.neighbors.append(map[n])
  return new_node

def clone(root):
    return deep_clone(root, {})
  
