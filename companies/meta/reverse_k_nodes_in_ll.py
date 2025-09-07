'''
LC 25: Reverse Nodes in k-Group
Given the head of a linked list, reverse the nodes of the list k at a time, 
and return the modified list. 
You may not alter the values in the list's nodes, only nodes themselves may be changed.
'''
from typing import Optional

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def _create_linked_list(self, arr):
        head, ptr = None, None
        for elem in arr:
            new_node = ListNode(elem)
            if ptr:
                ptr.next = new_node
                ptr = new_node
            else:
                head = new_node
                ptr = head
            
        return head

    def _print_linked_list(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        print (arr)
            

    def reverseLinkedList(self, head, k):
        new_head, ptr = None, head
        while k:
            next_node = ptr.next
            ptr.next = new_head
            new_head = ptr
            ptr = next_node
            k -= 1
        return new_head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ptr = head
        ktail, new_head = None, None
        while ptr:
            count = 0
            while count < k and ptr:
                ptr = ptr.next
                count += 1
            if count == k:
                revHead = self.reverseLinkedList(head, k)
                if not new_head:
                    new_head = revHead
                if ktail:
                    ktail.next = revHead
                ktail = head
                head = ptr
        if ktail:
            ktail.next = head
        return new_head if new_head else head
    
sol = Solution()
sol._print_linked_list(sol.reverseKGroup(sol._create_linked_list([1,2,3,4,5]), 2)) # [2,1,4,3,5]
sol._print_linked_list(sol.reverseKGroup(sol._create_linked_list([1,2,3,4,5]), 3)) # [3,2,1,4,5]     
