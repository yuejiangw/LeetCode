# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # use slow and fast pointers to find the middle point of the linked list
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        new_head = ListNode()
        new_link = slow.next
        slow.next = None
        while new_link:
            node = ListNode(new_link.val, new_head.next)
            new_head.next = node
            new_link = new_link.next

        p1, p2 = head, new_head.next
        while p1 and p2:
            next1 = p1.next
            next2 = p2.next
            p1.next = p2
            p2.next = next1
            p1 = next1
            p2 = next2
