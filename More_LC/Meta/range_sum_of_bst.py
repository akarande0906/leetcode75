'''
LC 938: Range Sum of BST: Given the root node of a binary search tree and two integers low and high, 
return the sum of values of all nodes with a value in the inclusive range [low, high].
         10
        /  \
       5    15
      / \     \
     3   7    18  for low = 7 and high = 15  => 10 + 5 + 7 + 15 = 32

'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum = 0
        def dst(node):
            nonlocal low, high, sum
            if not node:
                return
            if node.val >= low and node.val <= high:
                sum += node.val
            if low < node.val:
                dst(node.left)
            if high > node.val:
                dst(node.right)
        dst(root)
        return sum
    
    ''' BFS implementation
    sum = 0
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node.val >= low and node.val <= high:
                sum += node.val
            if node.left and low < node.val:
                # Call left subtree only if it could be included in the total
                q.append(node.left)
            if node.right and high > node.val:
                # Call right subtree only if it could be included in the total
                q.append(node.right)
        return sum
    '''
