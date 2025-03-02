'''
LC 203: Remove Linked List Elements
Remove all elements from a linked list of integers that have value val.
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def _create_linked_list(arr):
    head = ListNode()
    cur = head
    for a in arr:
        cur.next = ListNode(a)
        cur = cur.next
    return head.next

def _print_linked_list(head):
    cur = head
    while cur:
        print(cur.val, end=" ")
        cur = cur.next
    print()
    

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode()
        dummy_head.next = head
        cur, prev = head, dummy_head
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return dummy_head.next

removeElements = Solution().removeElements
_print_linked_list(removeElements(_create_linked_list([1,2,6,3,4,5,6]), 6))
_print_linked_list(removeElements(_create_linked_list([]), 1))
_print_linked_list(removeElements(_create_linked_list([7,7,7,7]), 7))
_print_linked_list(removeElements(_create_linked_list([7,7,7,7]), 1))

