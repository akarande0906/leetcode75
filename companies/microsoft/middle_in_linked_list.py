'''
Leetcode 876: Middle of Linked List
'''
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def _create_linked_list(self, array: List[int]) -> Optional[ListNode]:
        head = ListNode()
        cur_node = head
        for a in array:
            new_node = ListNode()
            new_node.val = a
            cur_node.next = new_node
            cur_node = new_node
        return head.next

    def _print_linked_list(self, head: Optional[ListNode]) -> None:
        cur_node = head
        print_str = []
        while cur_node:
            print_str.append(cur_node.val)
            cur_node = cur_node.next
        print (' '.join(str(print_str)))

            

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_ptr, fast_ptr = head, head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr
    
sol = Solution()

sol._print_linked_list(sol.middleNode(sol._create_linked_list([1,2,3,4,5])))
sol._print_linked_list(sol.middleNode(sol._create_linked_list([1,2,3,4,5,6])))

# Time Complexity: O(n), Space Complexity: O(1)