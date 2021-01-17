# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    此题的坑在于删除的结点若是头结点则要特殊处理
    """
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        pre, nex = None, head
        while nex:
            if nex.val == val:
                if nex == head:
                    head = head.next
                else:
                    pre.next = nex.next
                return head
            pre = nex
            nex = nex.next