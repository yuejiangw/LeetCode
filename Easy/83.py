# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    此题的坑在于末尾有连续重复元素的判断
    curr.next.next可能为None
    """
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        curr = head
        while curr.next != None:
            while curr.next.val == curr.val:
                if curr.next.next == None:
                    curr.next = None
                    return head
                else:
                    curr.next = curr.next.next
            curr = curr.next
        return head