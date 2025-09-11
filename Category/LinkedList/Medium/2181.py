# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head.next
        while curr and curr.val != 0:
            p = curr
            num = 0
            while p and p.val != 0:
                num += p.val
                p = p.next
            # p 指向下一个 0
            curr.val = num
            curr.next = p.next
            curr = p.next
        return head.next