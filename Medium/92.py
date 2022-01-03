# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """ 迭代 """
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy_head = ListNode(0, head)
        pre = dummy_head
        for _ in range(1, left):
            pre = pre.next
        head = pre.next
        for _ in range(right - left):
            nex = head.next
            head.next = nex.next
            nex.next = pre.next
            pre.next = nex
        return dummy_head.next



class Solution:
    """ 递归 """
    successor = None

    def reverseN(self, head, n):
        """ 翻转链表前 N 个结点，返回新的头结点 """
        if n == 1:
            self.successor = head.next
            return head
        last = self.reverseN(head.next, n - 1)
        head.next.next = head
        head.next = self.successor
        return last

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == 1:
            return self.reverseN(head, right)
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head
