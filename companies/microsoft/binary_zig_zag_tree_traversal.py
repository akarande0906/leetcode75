'''
Leetcode 103: Binary Tree Zigzag Level Order Traversal
'''
from typing import List, Optional
from collections import deque

#          3
#       /    \
#      9     20
#           /  \
#          15   7    
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def _create_tree(self, arr : Optional[List[int]]) -> TreeNode:
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


    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        queue = deque([root])
        right_flag = False
        traversed_array = []
        while queue:
            current_level = []
            n = len(queue)
            # If the right flag is set, pop from the right if not pop from the left
            for _ in range(n):
                node = queue.popleft() if not right_flag else queue.pop()
                if node:
                    current_level.append(node.val)
                    if right_flag: # We append to the left so we pop the right element first 
                        queue.appendleft(node.right)
                        queue.appendleft(node.left)
                    else:
                        queue.append(node.left)
                        queue.append(node.right)
            if current_level:
                traversed_array.append(current_level)
                right_flag = not right_flag # Toggle the right flag
        return traversed_array
    
sol = Solution()
print(sol.zigzagLevelOrder(sol._create_tree([3,9,20,None,None,15,7])))  
print(sol.zigzagLevelOrder(sol._create_tree([1])))
print(sol.zigzagLevelOrder(sol._create_tree([])))

