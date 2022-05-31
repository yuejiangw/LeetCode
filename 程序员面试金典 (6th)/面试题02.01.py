# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        duplicate = set()
        dummy_head = ListNode(None)
        dummy_head.next = head
        pre = dummy_head
        curr = head
        while curr:
            if curr.val not in duplicate:
                duplicate.add(curr.val)
                pre = curr
                curr = curr.next
            else:
                pre.next = curr.next
                curr = curr.next
        return dummy_head.next