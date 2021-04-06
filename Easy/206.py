# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        new_head = ListNode()
        curr = head
        while curr:
            if new_head.next == None:
                new_head.next = ListNode(curr.val)
            else:
                new_node = ListNode(curr.val, new_head.next)
                new_head.next = new_node
            curr = curr.next
        return new_head.next