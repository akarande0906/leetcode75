# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Create a Dict
        val_map = {}
        index = 0
        if not head:
            return False
        #iter = head
        while head:
            val_map[index] = head.val
            head = head.next
            index += 1
        id = 0
        max = index
        while (id < len(val_map)/2):
            if val_map[id] != val_map[max - id - 1]:
                return False
            id += 1
        return True
        
            

