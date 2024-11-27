'''
LC 173: Binary Search Tree iterator
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST)
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.cur = root
        self.stack = []
        # First add the left subtree to the stack. This will ensure that the smallest element is the first to pop
        self._inorder_processor(root)
        print (self.stack)

    # Utility function to add left subtree to the stack
    def _inorder_processor(self,node):
        while node:
            self.stack.append(node)
            node = node.left

    # Amortized time complexity: O(1) , Worst case O(n)
    def next(self) -> int:
        # Get the next smallest element
        top = self.stack.pop()
        # When we pop an element, we need to iterate through the right subtree and add its left elements
        # This is to maintain the order of the stack
        if top.right:
            self._inorder_processor(top.right)
        return top.val
             
    # Time complexity: O(1)
    def hasNext(self) -> bool:
        return len(self.stack) > 0

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
    
root = _create_tree([7,3,15,None,None,9,20])
'''
      7
    /  \ 
   3    15
        / \
       9  20
'''
iter = BSTIterator(root)
print (iter.next())
print (iter.next())
print (iter.hasNext())
print (iter.next())
print (iter.hasNext())
print (iter.next())
print (iter.hasNext())
print (iter.next())
print (iter.hasNext())

    

        

