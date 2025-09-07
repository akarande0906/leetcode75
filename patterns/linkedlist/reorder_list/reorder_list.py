# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head and head.next:
            slow = head
            fast = head
            prev = None
            while slow and fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
        
            prev.next = None
            prev = None
            while slow:
                next_node = slow.next
                slow.next = prev
                prev = slow
                slow = next_node
            curr = head
            while prev and curr:
                temp = curr.next
                curr.next = prev
                curr = prev
                prev = temp

