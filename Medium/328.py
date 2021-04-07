# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
            
        odd_head = ListNode(None)
        odd_tail = odd_head
        even_head = ListNode(None)
        even_tail = even_head
        curr = head
        count = 1
        while curr:
            # 奇数结点
            if count % 2 == 1:
                odd_tail.next = ListNode(curr.val)
                odd_tail = odd_tail.next
            # 偶数结点
            else:
                even_tail.next = ListNode(curr.val)
                even_tail = even_tail.next
            count += 1
            curr = curr.next
        # 拼接两条链表
        odd_tail.next = even_head.next
        return odd_head.next