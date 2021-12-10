# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        curr = head
        p1 = l1
        p2 = l2
        while p1 and p2:
            if p1.val < p2.val:
                curr.next = ListNode(p1.val)
                p1 = p1.next
            else:
                curr.next = ListNode(p2.val)
                p2 = p2.next
            curr = curr.next
        if p1:
            curr.next = p1
        if p2:
            curr.next = p2
        return head.next
