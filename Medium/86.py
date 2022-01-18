# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    建立两条链表，一条保存小于 x 的所有节点，一条保存大于等于 x 的所有节点，
    之后把第一条链表的末尾链接在第二条链表的头部，返回第一条链表的头部即可
    T: O(n) S: O(1)
    """

    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next:
            return head

        small, large = ListNode(), ListNode()
        curr = head
        p_small, p_large = small, large
        while curr:
            v = curr.val
            if v < x:
                p_small.next = curr
                curr = curr.next
                p_small = p_small.next
                p_small.next = None
            else:
                p_large.next = curr
                curr = curr.next
                p_large = p_large.next
                p_large.next = None
        p_small.next = large.next
        return small.next
