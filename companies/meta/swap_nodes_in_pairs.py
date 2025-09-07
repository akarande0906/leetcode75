'''
LC 24: Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head.
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def _create_linked_list_(arr):
    head = ListNode()
    node = head
    for elem in arr:
        node.next = ListNode(elem)
        node = node.next
    return head.next

def _print_linked_list_(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        temp_head = ListNode()
        temp_head.next = head
        node = temp_head
        while node:
            first_node = node.next
            second_node = node.next.next if node.next else None
            if first_node and second_node:
                node.next, second_node.next, first_node.next = second_node, first_node, second_node.next
                node = first_node
            else:
                node = None
        return temp_head.next
# Time Complexity: O(N) where N is the number of nodes in the linked list
# Space Complexity: O(1) as we are using constant space

# Test Cases
_print_linked_list_ (Solution().swapPairs(_create_linked_list_([1,2,3,4,5,6,7,8,9,10])))
_print_linked_list_ (Solution().swapPairs(_create_linked_list_([1,2,3,4,5,6,7,8,9])))
_print_linked_list_ (Solution().swapPairs(_create_linked_list_([1,2,3,4,5,6,7])))
_print_linked_list_ (Solution().swapPairs(_create_linked_list_([1])))
_print_linked_list_ (Solution().swapPairs(_create_linked_list_([])))
                

                