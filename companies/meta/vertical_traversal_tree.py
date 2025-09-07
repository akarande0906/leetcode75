'''
LC 314: Binary Tree Vertical Tree Order Traversal
'''
from collections import defaultdict
from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []
        columnMap = defaultdict(list)
        # Min and Max columns are used to track the left and right ranges 
        # with 0 being the root column
        min_column, max_column = 0, 0
        q = deque()
        q.append((root, 0))
        while q:
            node, col = q.popleft()
            if node is not None:
                columnMap[col].append(node.val)
                min_column = min(min_column, col)
                max_column = max(max_column, col)
                q.append((node.left, col - 1))
                q.append((node.right, col + 1))
        return_list = []
        for col in range(min_column, max_column + 1):
            if col in columnMap:
                return_list.append(columnMap[col])
        print (return_list)
        return return_list

'''
         3
        / \
       9  20
         /  \
         15  7   => [[[9],[3,15],[20],[7]]
'''


