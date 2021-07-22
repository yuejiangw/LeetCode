# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = ListNode()
        p = head
        while p is not None:
            p1 = p.next
            p.next = new_head.next
            new_head.next = p
            p = p1
        return new_head.next
