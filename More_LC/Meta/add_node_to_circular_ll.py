'''
LC 708: Insert Into Sorted Circular Linked List
Given a Circular Linked List node, which is sorted in non-descending order, 
write a function to insert a value insertVal into the list such that it remains a sorted circular list. 
The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list.
If there are multiple suitable places for insertion, you may choose any place to insert the new value. 
After the insertion, the circular list should remain sorted.
If the list is empty (i.e., the given node is null), you should create a new single circular list and return the reference to that single node. 
Otherwise, you should return the originally given node.
'''


from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal)
            head.next = head
        elif head == head.next:
            node = Node(insertVal)
            head.next = node
            node.next = head
        else:
            minval = float('inf')
            minhead = None
            cur = head
            visited = set()
            while not cur in visited:
                if cur.val < minval:
                   minval = cur.val
                   minhead = cur
                visited.add(cur)
                cur = cur.next
            prev, cur = head, head.next
            while True:
                if (
                    (prev.val <= insertVal and insertVal <= cur.val) or
                    (cur == minhead and (cur.val >= insertVal or prev.val <= insertVal))
                ):
                    node = Node(insertVal, cur)
                    prev.next = node
                    break
                prev, cur = cur, cur.next
        return head   
    
    # ---- Better Solution --- 
    """
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insertNewNode(self, node, insertVal):
        insertNode = Node(insertVal)
        insertNode.next = node.next
        node.next = insertNode

    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        elif head == head.next:
            node = Node(insertVal)
            head.next = node
            node.next = head
            return head
        else:
            cur = head
            while cur.next != head:
                if cur.val <= insertVal and cur.next.val >= insertVal:
                    break
                elif cur.val > cur.next.val: 
                    if (cur.next.val >= insertVal or cur.val <= insertVal): 
                        # At this point we have reached the end of the loop and 
                        # we are iterating between the max and min element of the list
                        break
                cur = cur.next
        self.insertNewNode(cur, insertVal)
        return head


            