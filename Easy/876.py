# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getLength(self, head: ListNode) -> ListNode:
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

    def middleNode(self, head: ListNode) -> ListNode:
        length = self.getLength(head)
        target = length // 2
        count = 0
        curr = head
        while count < target:
            curr = curr.next
            count += 1
        return curr