'''
Given the root of a binary tree, display the node values at each level. Node values for all levels should be displayed on separate lines. Let’s take a look at the below binary tree.
'''
# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
from collections import deque 
def level_order_traversal(root):
    result = []
    # Replace this placeholder return statement with your code
    if not root:
       return None
    que = deque()
    que.append(root)
    while que:
        n = len(que)                  
        arr = []
        for _ in range(n):
          node = que.popleft()
          arr.append(str(node.data))
          if node.left:
             que.append(node.left)
          if node.right:
             que.append(node.right)
        result.append(', '.join(arr))
    return "; ".join(result)
 
'''
Example OP: 
25, 75, 350	100; 50, 200; 25, 75, 350
'''
