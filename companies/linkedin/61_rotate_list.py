# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        # Find the length of the linked list
        leng = 1
        last = head
        while last.next:
            last = last.next
            leng += 1
        k = k % leng
        # Becomes circular
        last.next = head
        cur = head
        for _ in range(leng - k - 1):
            cur = cur.next
        new_head = cur.next
        cur.next = None
        return new_head
            
def populateList(arr):
    head, cur = None, None
    for val in arr:
        if not head:
            head = ListNode(val)
            cur = head
        else:
            node = ListNode(val)
            cur.next = node
            cur = cur.next
    return head

def printList(listNode): 
    cur = listNode
    arr = []
    while cur:
        arr.append(cur.val)
        cur = cur.next
    print (arr)



printList(Solution().rotateRight(populateList([1,2,3,4,5]), 2))
printList(Solution().rotateRight(populateList([0,1,2]), 2))

        
        
            
        
