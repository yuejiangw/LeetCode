# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        dummy_head = ListNode(0, head)
        last, mid, first = dummy_head, head, head.next
        count = 0

        while first:
            if count % 2 == 0:
                mid.next = first.next
                first.next = mid
                last.next = first
                mid, first = first, mid
            last = last.next
            mid = mid.next
            first = first.next
            count += 1
        return dummy_head.next


# 2024.04.12

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 快慢指针, fast 一次走一步, slow 一次走两步
        # 如果有环的话 fast 指针一定会追上 slow 指针
        # 之后再把快指针重新放在链表头部一次走一步, 第二次相遇的位置就是环的起点
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return fast
        return None