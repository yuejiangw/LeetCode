# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_length(self, head):
        counter = 0
        curr = head
        tail = curr
        while curr is not None:
            counter += 1
            tail = curr
            curr = curr.next
        return tail, counter

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None:
            return head
        tail, length = self.get_length(head)
        if k % length == 0:
            return head
        num_to_head = length - k % length
        curr = head
        pre = curr
        while num_to_head > 0:
            pre = curr
            curr = curr.next
            num_to_head -= 1
        pre.next = None
        tail.next = head
        return curr
    