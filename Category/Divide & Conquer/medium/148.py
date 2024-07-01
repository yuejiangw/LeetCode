# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # T: O(nlogn)
        # S: O(logn)
        if not head or not head.next:
            return head
        # split linked list into two parts
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        # merge sort
        return self.merge(left, right)
    
    def getMid(self, head):
        pre = None
        slow, fast = head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        return slow
    
    def merge(self, h1, h2):
        p1, p2 = h1, h2
        dummy = ListNode()
        curr = dummy
        while p1 and p2:
            if p1.val <= p2.val:
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next
            curr = curr.next
        curr.next = p1 if p1 else p2
        return dummy.next