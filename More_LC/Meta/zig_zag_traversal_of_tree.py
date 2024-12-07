'''
LC 103: Zigzag Level Order traversal of Binary Tree
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).
                   3
                 /    \
                9      20 
                      /  \
                     15   7  => [[3], [20,9], [15,7]]
'''
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
        # To go zigzag we have to include a flag that goes in opposite directions
        queue = deque()
        queue.append(root)
        right_flag = False
        return_arr = []
        while queue:
            cur_arr = []
            n = len(queue)
            for i in range(n):
                if right_flag:
                    node = queue.pop()
                else:
                    node = queue.popleft()
                if node:
                    cur_arr.append(node.val)
                    if right_flag:
                        queue.appendleft(node.right)
                        queue.appendleft(node.left)
                    else:
                        queue.append(node.left)
                        queue.append(node.right)
            if cur_arr:
                return_arr.append(cur_arr)
            right_flag = not right_flag
        return return_arr
    
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


zigzag = Solution().zigzagLevelOrder
print (zigzag(_create_tree([3,9,20,None,None,15,7])))
print (zigzag(_create_tree([3,9,20,4,21,15,7,12,2,1,4])))
print (zigzag(_create_tree([])))
print (zigzag(_create_tree([1])))

        