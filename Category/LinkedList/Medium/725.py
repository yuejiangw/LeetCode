# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        def getLength(head):
            l = 0
            curr = head
            while curr:
                l += 1
                curr = curr.next
            return l
        
        if not head:
            return [head for _ in range(k)]

        l = getLength(head)
        res = []
        group_len = l // k
        extra = l % k

        pre = curr = head
        for _ in range(k):
            for _ in range(group_len):
                pre = curr
                curr = curr.next
            if extra > 0:
                pre = curr
                curr = curr.next
                extra -= 1
            pre.next = None
            res.append(head)
            head = curr
        return res