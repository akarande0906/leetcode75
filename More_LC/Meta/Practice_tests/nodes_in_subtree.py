

from collections import deque


class Node: 
  def __init__(self, data): 
    self.val = data 
    self.children = []


# Add any helper functions you may need here
def traverse_subtree(root, query, s):
  queue = deque()
  queue.append(root)
  index = 0
  found_node = False
  node_count = 0
  while queue:
    node = queue.popleft()
    if node.val == query[0]:
      # We need to start at this subtree and continue
      # reset the queue and start here
      queue.clear()
      found_node = True
    if found_node and s[node.val - 1] == query[1]:
        node_count += 1
    for child in node.children:
      queue.append(child)
  return node_count
      

def count_of_nodes(root, queries, s):
  if not root:
    return []
  ret_arr = []
  for q in queries:
    ret_arr.append(traverse_subtree(root, q, s))
  return ret_arr

# Test data
s_1 = "aba"
root_1 = Node(1) 
root_1.children.append(Node(2)) 
root_1.children.append(Node(3)) 
queries_1 = [(1, 'a')]
print (count_of_nodes(root_1, queries_1, s_1))

s_2 = "abaacab"
root_2 = Node(1)
root_2.children.append(Node(2))
root_2.children.append(Node(3))
root_2.children.append(Node(7))
root_2.children[0].children.append(Node(4))
root_2.children[0].children.append(Node(5))
root_2.children[1].children.append(Node(6))
queries_2 = [[1, 'a'],[2, 'b'],[3, 'a']]
print (count_of_nodes(root_2, queries_2, s_2))
