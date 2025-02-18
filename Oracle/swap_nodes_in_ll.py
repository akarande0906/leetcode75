'''
LC 1721: Swapping Nodes in a Linked List
'''
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def _create_linked_list(arr):
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head

def _print_linked_list(head):
    cur = head
    while cur:
        print(cur.val, end=" ")
        cur = cur.next
    print()

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Find the length of the linked list and then traverse to the 
        # kth and the len - kth elements and swap them.
        cur = head
        llen = 0
        while cur:
            cur = cur.next
            llen += 1 
        rev_k = llen - k + 1
        if rev_k == k: 
            return head
        cur = head
        id = 1
        nodek, noderev = None, None
        while cur:
            if nodek and noderev:
                break
            if id == k:
                nodek = cur
            elif id == rev_k:
                noderev = cur
            cur = cur.next
            id += 1
        nodek.val, noderev.val = noderev.val, nodek.val
        return head
# Time: O(n)
# Space: O(1)

# Alternate Solution: Single Pass
    def swapNodes_SP(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Find the length of the linked list and then traverse to the 
        # kth and the len - kth elements and swap them.
        start_node, end_node = None, None
        id = 1
        cur = head
        while cur:
            if end_node:
                end_node = end_node.next
            if id == k:
                start_node = cur
                end_node = head
            cur = cur.next
            id += 1
        start_node.val, end_node.val = end_node.val, start_node.val
        return head
        
        
        

# swap = Solution().swapNodes
swap = Solution().swapNodes_SP
_print_linked_list(swap(_create_linked_list([1,2,3,4]), 1))
_print_linked_list(swap(_create_linked_list([1,2,3,4,5]), 2))
_print_linked_list(swap(_create_linked_list([7,9,6,6,7,8,3,0,9,5]), 5))
        
        
        