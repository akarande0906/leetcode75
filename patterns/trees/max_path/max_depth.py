class b_tree:
   def __init__(self, val = 0):
       self.val = val
       self.left = None
       self.right = None

def dfs(node):
    if node is None:
       return 0
    else:
       return 1 + max(dfs(node.left), dfs(node.right))

def _create_tree(arr):
   if not arr:
      return None
   root = b_tree(arr[0])
   n = len(arr)
   q = [root]
   i = 1
   while i < n:
      node = q.pop(0)
      if arr[i] is not None:
          node.left = b_tree(arr[i])
          q.append(node.left)
      i += 1
      if arr[i] is not None and i < n:
          node.right = b_tree(arr[i])
          q.append(node.right)
      i += 1
   return root
           
         

arr = [3,9,20,None,None,15,7]
root = _create_tree(arr)
print(dfs(root))

