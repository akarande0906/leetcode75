from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Complexity: T: O(N), S: O(N)

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> list[int]:
        retarr = [root.val]
        stack = []

        def iterateLeftTree(root):
            if not root or (not root.left and not root.right):
                return
            retarr.append(root.val)
            if root.left:
                iterateLeftTree(root.left)
            else:
                iterateLeftTree(root.right)

        def iterateLeafNodes(root):
            if not root:
                return
            if not root.left and not root.right:
                retarr.append(root.val)
            else:
                if root.left:
                    iterateLeafNodes(root.left)
                if root.right:
                    iterateLeafNodes(root.right)

        def iterateRightTree(root):
            if not root or (not root.left and not root.right):
                return
            stack.append(root.val)
            if root.right:
                iterateRightTree(root.right)
            else:
                iterateRightTree(root.left)
        
        iterateLeftTree(root.left)
        if root.left or root.right:
            iterateLeafNodes(root)
        iterateRightTree(root.right)
        while stack:
            retarr.append(stack.pop())
        return retarr

def createTree(arr):
    if not arr:
        return None
    q = deque()
    root = TreeNode(arr[0])
    q.append(root)
    n = 1
    while q and n < len(arr):
        print (n)
        node = q.popleft()
        if arr[n]:
            left = TreeNode(arr[n])
            node.left = left
            q.append(left)
        n += 1
        if arr[n]:
            right = TreeNode(arr[n])
            node.right = right
            q.append(right)
        n += 1
    return root


arr = [1,2,3,4,5,6,None,None,None,7,8,9,10]
print(Solution().boundaryOfBinaryTree(createTree(arr)))

