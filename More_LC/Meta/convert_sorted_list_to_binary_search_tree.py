'''
LC 109: Convert Sorted List to Binary Search Tree
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a 
height-balanced
binary search tree.
E.g. [-10] -> [-3] -> [0] -> [5] -> [9] 
==>                    0 
                    /     \
                  -3       9
                  /        /
                -10       5    
'''
from typing import Optional
from collections import deque
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def mapListToArray(head):
            vals = []
            while head:
                vals.append(head.val)
                head = head.next
            return vals
        values = mapListToArray(head)
    
        def recurseBST(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(values[mid])
            if left == right:
                return node
            node.left = recurseBST(left, mid - 1)
            node.right = recurseBST(mid + 1, right)
            return node
        return recurseBST(0, len(values) - 1)
    
def _create_linked_list(array):
    head = cur = None
    for n in array:
        if not head:
            head = ListNode(n)
            cur = head
        else:
            prev = cur
            cur = ListNode(n)
            prev.next = cur
    return head

def _traverse_tree_pre_order(root):
    if not root:
        return []
    return_arr = []
    queue = deque()
    queue.append(root)
    while queue:
        n = len(queue)
        node = queue.popleft()
        return_arr.append(node.val)
        if not node.left and n:
            return_arr.append(None)
        elif node.left:
            queue.append(node.left)
        if not node.right and n:
            return_arr.append(None)
        else:
            queue.append(node.right) 
    return return_arr

'''
Time Complexity: O(n)  as we convert to array  SC: O(n)
'''


''' Alternate solution : In order traversal: TC : O(n)    SC: O(logn)
def findSize(head):
            ptr = head
            c = 0
            while ptr:
                ptr = ptr.next
                c += 1
            return c

        def convert(left, right):
            nonlocal head
            if left > right:
                return None
            mid = (left + right) // 2
            left = convert(left, mid - 1)
            node = TreeNode(head.val)
            node.left = left
            head = head.next
            node.right = convert(mid+1, right)
            return node
    
        size = findSize(head)
        return convert(0, size - 1)
'''


tree = Solution().sortedListToBST(_create_linked_list([-10,-3,0,5,9]))
print (_traverse_tree_pre_order(tree))



            
    


