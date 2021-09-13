# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        new_head = ListNode(None, head)
        pre = new_head
        curr = new_head.next
        while curr is not None:
            while curr is not None and curr.val == val:
                pre.next = curr.next
                curr = curr.next
            pre = curr
            if curr is not None:
                curr = curr.next
        return new_head.next 