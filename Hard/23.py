# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import List

class Solution:
    def to_list(self, head):
        curr = head
        res = []
        while curr:
          res.append(curr.val)
          curr = curr.next
        return res

    def list_to_link(self, l):
        head = ListNode()
        curr = head
        for num in l:
            curr.next = ListNode(num)
            curr = curr.next
        return head.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        nums = []
        for i in range(len(lists)):
            nums += self.to_list(lists[i])
        nums.sort()
        return self.list_to_link(nums)
