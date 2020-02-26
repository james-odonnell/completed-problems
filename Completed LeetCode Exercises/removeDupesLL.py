# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        currentNode = head
        while currentNode is not None and currentNode.next is not None:
            if currentNode.val == currentNode.next.val:
                currentNode.next = currentNode.next.next
            else:
                currentNode = currentNode.next

        currentNode = head
        while currentNode is not None:
            return currentNode







node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(1)
node4 = ListNode(2)
node5 = ListNode(3)
node6 = ListNode(3)


node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

head = node1
currentNode = head



