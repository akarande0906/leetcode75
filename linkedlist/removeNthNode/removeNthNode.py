# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        max = 0
        cur = head
        while cur:
            max += 1
            cur = cur.next
        if max == n:
            head = head.next
        elif max == 0:
            return None
        n = max - n + 1 # from the left 
        cntr = 1
        cur = head
        while cur and cur.next:
            if cntr == n - 1:
                cur.next = cur.next.next
                break
            cntr += 1
            cur = cur.next
        return head
