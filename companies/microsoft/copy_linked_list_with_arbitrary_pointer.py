'''
Leetcode 138: Copy List with Ramdom Pointer
'''
from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # First iterate over the linked list and construct the new linked list
        # Here we copy the random pointer as is, but map current nodes to the new cloned nodes
        mapper = {}
        def _copy_node(self, old):
            new_node = Node(old.val)
            new_node.random = old.random
            self.mapper[old] = new_node
            return new_node
        
        def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
            # First make a copy and store the mapping of the random pointer 
            new_head = Node(-1) # Dummy head
            cur, new_cur = head, new_head
            while cur:
                new_node = self._copy_node(cur)
                new_cur.next = new_node
                new_cur = new_node
                cur = cur.next
            new_cur = new_head
            while new_cur:
                # Now use the map to set the correct random node
                if new_cur.random:
                    new_cur.random = self.mapper[new_cur.random]
                new_cur = new_cur.next
            return new_head.next
