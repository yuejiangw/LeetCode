# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        tmp = []
        curr = head
        while curr:
            tmp.append(curr.val)
            curr = curr.next
        i = 0
        j = len(tmp) - 1
        while i < j:
            if tmp[i] != tmp[j]:
                return False
            i += 1
            j -= 1
        return True