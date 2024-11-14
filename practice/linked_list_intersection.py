'''
LC: 160
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited_set = set()
        cur = headA
        while cur:
            if cur not in visited_set:
                visited_set.add(cur)
            cur = cur.next

        cur = headB
        while cur:
            if cur in visited_set:
                return cur
            cur = cur.next
        return None
