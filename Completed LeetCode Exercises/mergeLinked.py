# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head1 = l1
        head2 = l2
        b = []
        while head1 is not None:
            b.append(head1.val)
            head1 = head1.next

        while head2 is not None:
            b.append(head2.val)
            head2 = head2.next
        b.sort()
        if len(b) > 0:
            head = ListNode(b[0])
        else:
            return None
        currentNode = head
        for ele in b[1:]:
            currentNode.next = ListNode(ele)
            currentNode = currentNode.next

        while head is not None:
            return head
