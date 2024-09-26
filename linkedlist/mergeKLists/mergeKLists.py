# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                node1 = lists[i]
                node2 = lists[i+1] if i + 1 < len(lists) else None
                mergedList.append(self.mergeLists(node1, node2))
            lists = mergedList
        return lists[0]

    def mergeLists(self, node1: [Optional[ListNode]], node2: [Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        currentNode = dummy
        while node1 and node2:
            if node1.val <= node2.val:
                currentNode.next = node1
                node1 = node1.next
            else:
                currentNode.next = node2
                node2 = node2.next
            currentNode = currentNode.next
        currentNode.next = node1 if node1 else node2
        return dummy.next
        
