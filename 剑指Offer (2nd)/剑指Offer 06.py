# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        nums = []
        curr = head
        while curr != None:
            nums.append(curr.val)
            curr = curr.next
        return nums[::-1]