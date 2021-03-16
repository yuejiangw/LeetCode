# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 弗洛伊德判圈法
# 设计两个快慢指针，快指针一次走两步，慢指针一次走一步
# 初始位置都在链表开头，如果有圈，则必定两个指针会有一次相遇
# 此时再将快指针重新拨回起始位置，然后一次走一步
# 则第二次相遇的位置就是环的起点
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while True:
            if not fast or not fast.next:
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast