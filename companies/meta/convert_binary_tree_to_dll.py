'''
LC 426: Convert Binary Search Tree to Sorted Doubly Linked List
Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

Use in-order traversal to sort from least to most 
'''


from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        head, tail = None, None

        def inOrderTraversal(node):
            nonlocal head, tail
            if not node:
                return
            inOrderTraversal(node.left)
            if not tail:
                head = node
            else:
                tail.right = node
                node.left = tail
            tail = node
            inOrderTraversal(node.right)
        if not root:
            return None
        inOrderTraversal(root)

        head.left = tail
        tail.right = head

        return head
    
    def _create_tree(self, arr):
        if not arr:
            return None
        root = Node(arr[0])
        n = len(arr)
        q = [root]
        i = 1
        while i < n:
            node = q.pop(0)
            if arr[i] is not None:
                node.left = Node(arr[i])
                q.append(node.left)
            i += 1
            if arr[i] is not None and i < n:
                node.right = Node(arr[i])
                q.append(node.right)
            i += 1
        return root
    
    def traverseLinkedList(self, head):
        ret_arr = []
        if not head:
            return []
        cur = head
        while cur:
            ret_arr.append(cur.val)
            cur = cur.right
            if cur == head:
                break
        return ret_arr 
    

sol = Solution()
print (sol.traverseLinkedList(sol.treeToDoublyList(sol._create_tree([4,2,5,1,3]))))
print (sol.traverseLinkedList(sol.treeToDoublyList(sol._create_tree([2,1,3]))))
    

        