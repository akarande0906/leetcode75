'''
Leetcode 206: Reverse Linked List
'''
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def _create_linked_list(self, linked_list_array: List[int]) -> ListNode:
        if not linked_list_array:
            return None
        dummyHead = ListNode()
        cur_node = dummyHead
        for elem in linked_list_array:
            new_node = ListNode()
            new_node.val = elem
            cur_node.next = new_node
            cur_node = new_node
        return dummyHead.next
    
    def _print_linked_list(self, root: ListNode) -> None:
        if not root:
            print ('')
        temp_array = []
        while root:
            temp_array.append(str(root.val))
            root = root.next
        print (','.join(temp_array))
    

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self._print_linked_list(head)
        cur = head
        prev = None
        while cur:
            next_node = cur.next
            cur.next = prev
            cur, prev = next_node, cur
        self._print_linked_list(prev)
           
        


sol = Solution()
sol.reverseList(sol._create_linked_list([1,2,3,4,5]))
sol.reverseList(sol._create_linked_list([1,2]))
sol.reverseList(sol._create_linked_list([]))



            