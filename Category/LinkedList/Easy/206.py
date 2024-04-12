# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """ 迭代解法 """
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = ListNode()
        p = head
        while p is not None:
            p1 = p.next
            p.next = new_head.next
            new_head.next = p
            p = p1
        return new_head.next


class Solution:
    """ 递归解法 """
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or head.next == None:
            return head

        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last
