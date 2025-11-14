# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head
        curr = head
        prev = None
        for i in range(left-1):
            prev = curr
            curr = curr.next
        last = prev
        new_end = curr
        next = curr.next
        for i in range(right - left + 1):
            curr.next = prev
            prev = curr
            curr = next
            if next != None:
                next = next.next
        if last != None:
            last.next = prev
        else:
            head = prev
        new_end.next = curr
        return head


# Reverse LL from middle
