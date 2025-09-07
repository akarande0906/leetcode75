'''
LC 987:  Vertical Order Traversal of a Binary Tree
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.
For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).
The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.
Return the vertical order traversal of the binary tree.
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
    def verticalTraversal(self, root: Optional[TreeNode]) -> list[list[int]]:
        vertical_map = defaultdict(list)
        min_level = float('inf')
        max_level = float('-inf')
        queue = deque()
        queue.append((root, 0))
        while queue:
            n = len(queue)
            temp_map = defaultdict(list)
            for n in range(len(queue)):
                node,level = queue.popleft()
                temp_map[level].append(node.val)
                min_level = min(level, min_level)
                max_level = max(level, max_level)
                if node.left:
                    queue.append((node.left, level - 1))
                if node.right:
                    queue.append((node.right, level + 1))
            for key, val in temp_map.items():
                vertical_map[key].extend(sorted(val))
        result_arr = []
        for iter in range (min_level, max_level + 1):
            result_arr.append(vertical_map[iter])
        return result_arr
    
# Utility function to create Tree structure from array
def _create_tree(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    n = len(arr)
    q = [root]
    i = 1
    while i < n:
        node = q.pop(0)
        if arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1
        if arr[i] is not None and i < n:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1
    return root

vert = Solution().verticalTraversal
print(vert(_create_tree([3,9,20,None,None,15,7])))
print(vert(_create_tree([1,2,3,4,5,6,7])))
print(vert(_create_tree([1,2,3,4,6,5,7])))
print(vert(_create_tree([0,None,1])))


            




        