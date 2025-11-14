
from typing import Optional 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base Case
        if not head or not head.next:
            return head

        # Recursive Call
        node = self.reverseList(head.next)

        # Reversing Pointers
        head.next.next = head
        head.next = None

        # Return Node
        return node
