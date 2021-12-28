# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """ 新建一个链表 """
        if head == None:
            return None
        if head.next == None:
            return head
        curr = head
        new_head = ListNode(None)
        while curr != None:
            if new_head.next == None:
                new_head.next = ListNode(curr.val)
            else:
                tmp = ListNode(curr.val)
                tmp.next = new_head.next
                new_head.next = tmp
            curr = curr.next
        return new_head.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """ inplace 操作 """
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        curr = head
        next = None
        while curr:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
        return pre
