# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, a, b):
        """ reverse nodes in the range of [a, b) """
        pre = None
        curr = a
        nex = a
        while curr != b:
            nex = curr.next
            curr.next = pre
            pre = curr
            curr = nex
        # return the head node of the reversed linked list
        return pre

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        a, b = head, head
        for i in range(k):
            # total nodes in the linked list is less than k, no need to reverse.
            if not b:
                return head
            b = b.next
        new_head = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return new_head
