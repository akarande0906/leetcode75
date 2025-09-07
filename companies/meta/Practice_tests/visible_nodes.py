


from collections import deque
# Add any extra import statements you may need here


class TreeNode: 
  def __init__(self,key): 
    self.left = None
    self.right = None
    self.val = key 

def _create_tree(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    n = len(arr)
    q = [root]
    i = 1
    while i < n:
        if q:
            node = q.pop(0)
        if arr[i] is not None and node:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1
        if i < n and arr[i] is not None and node:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1
    return root


def visible_nodes(root):
  total_nodes = 0
  if not root:
    return 0
  queue = deque()
  queue.append(root)
  while queue:
    level_len = len(queue)
    if level_len:
      total_nodes += 1
      for _ in range(level_len):
        node = queue.popleft()
        if node.left:
           queue.append(node.left)
        if node.right:
           queue.append(node.right)
  return total_nodes

root = _create_tree([8,3,10,1,6,None,14,None,None,4,7,13])
print(visible_nodes(root))
root = _create_tree([10,8,15,4,None,14,16,None,5,None,None,None,None,None,None,None,None,None,6])
print(visible_nodes(root))

