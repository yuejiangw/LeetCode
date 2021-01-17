# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getLength(self, head: ListNode) -> int:
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

    def kthToLast(self, head: ListNode, k: int) -> int:
        length = self.getLength(head)
        curr = head
        for i in range(0, length - k):
            curr = curr.next
        return curr.val