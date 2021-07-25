# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1, p2 = headA, headB
        while (p1 != p2):
            if p1 != None:
                p1 = p1.next
            else:
                p1 = headB
            if p2 != None:
                p2 = p2.next
            else:
                p2 = headA
        return p1
        
        