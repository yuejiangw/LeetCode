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


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        '''
        left = 2, right = 4
            pre   4 ->  3
                        \
        dummy -> 1     -> 2  -> (None)              5
            reverse_pre                               cur
        '''
        dummy_head = ListNode(0, head)
        pre = dummy_head
        for _ in range(1, left):
            pre = pre.next
        # curr 所在位置即为 left 
        curr = pre.next
        reverse_pre = pre
        pre = None
        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = pre
            pre = curr
            curr = next_node
        
        reverse_pre.next.next = curr
        reverse_pre.next = pre

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
