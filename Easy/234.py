# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values == values[::-1]
