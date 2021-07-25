# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_len(self, head: ListNode) -> int:
        curr = head
        result = 0
        while curr:
            curr = curr.next
            result += 1
        return result

    def middleNode(self, head: ListNode) -> ListNode:
        length = self.get_len(head)
        target_len = length // 2 + 1
        curr = head
        counter = 1
        while counter < target_len:
            curr = curr.next
            counter += 1
        return curr