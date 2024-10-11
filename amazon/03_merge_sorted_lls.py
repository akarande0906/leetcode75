'''
Given two sorted linked lists, merge them so that the resulting linked list is also sorted. 
'''

class LinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def merge_lists(head1, head2):
    head, cur, node = None, None, None
    
    while head1 and head2:
      if head1.data < head2.data:
          node = LinkedListNode(head1.data)
          head1 = head1.next
      else:
        node = LinkedListNode(head2.data)
        head2 = head2.next
      if not head:
        head = node
        cur = head
      else:
        cur.next = node
        cur = cur.next
    if head1 and not head2:
      while head1:
        cur.next = head1
        head1 = head1.next
        cur = cur.next
    elif head2 and not head1:
      while head2:
        cur.next = head2
        head2 = head2.next
        cur = cur.next
    # Replace this placeholder return statement with your code
    return head


def create_linked_list(arr):
    head = None
    cur = None
    for i in arr:
       node = LinkedListNode(i)
       if not head:
          head = node
          cur = head
       else: 
          cur.next = node
          cur = cur.next
    return head

def print_linked_list(head):
   arr = []
   while head:
     arr.append(head.data)
     head = head.next
   print(arr)


if __name__ == '__main__':
   head1 = create_linked_list([4, 8, 15, 19, 22])
   head2 = create_linked_list([7, 9, 10, 16])
   head = merge_lists(head1, head2)
   print_linked_list(head)
