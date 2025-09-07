'''
LC 116: Populating Next Right Pointers in Each Node
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

'''
from collections import deque
from typing import Optional

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        queue = deque()
        queue.append(root)
        while queue:
            n = len(queue)
            prev = queue.popleft()
            if prev.left:
                queue.append(prev.left)
            if prev.right:
                queue.append(prev.right)
            if n == 1:
                prev.next = None
            else:
                for i in range(1, n):
                    cell = queue.popleft()
                    prev.next = cell
                    if cell.left:
                        queue.append(cell.left)
                    if cell.right:
                        queue.append(cell.right)
                    if i == n - 1:
                        cell.next = None
                    else:
                        prev = cell
        return root