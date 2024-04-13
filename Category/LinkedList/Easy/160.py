# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    '''
    错的人迟早会走散，而对的人迟早会相遇
    '''
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        p_a, p_b = headA, headB
        while p_a != p_b:
            if p_a:
                p_a = p_a.next
            else:
                p_a = headB
            
            if p_b:
                p_b = p_b.next
            else:
                p_b = headA
        return p_a