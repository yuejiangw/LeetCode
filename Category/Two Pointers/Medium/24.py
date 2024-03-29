# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        dummy_head = ListNode(0, head)
        last, mid, first = dummy_head, head, head.next
        count = 0

        while first:
            if count % 2 == 0:
                mid.next = first.next
                first.next = mid
                last.next = first
                mid, first = first, mid
            last = last.next
            mid = mid.next
            first = first.next
            count += 1
        return dummy_head.next
