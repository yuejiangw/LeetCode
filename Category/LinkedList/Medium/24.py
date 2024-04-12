# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy_head = ListNode(0, head)
        pre, mid, curr = dummy_head, head, head.next
        count = 0
        while curr:
            if count % 2 == 0:
                mid.next = curr.next
                curr.next = mid
                pre.next = curr
                # update pointers
                curr = mid.next
                pre = pre.next
            else:
                pre = mid
                mid = curr
                curr = curr.next
            count += 1
        return dummy_head.next
