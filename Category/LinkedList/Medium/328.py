# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge case
        if not head or not head.next:
            return head
        count = 1
        curr = head
        pre = None
        # 暂存偶数节点的 sublist
        dummy_even_head = ListNode()
        p = dummy_even_head
        while curr:
            if count % 2 == 1:
                pre = curr
                curr = curr.next
            else:
                # 暂存下一个节点
                tmp = curr.next
                # 把 even node 挂在 dummy_even_head 上
                pre.next = curr.next
                p.next = curr
                curr.next = None
                p = p.next
                # 更新 curr
                curr = tmp
            count += 1
        # 由于遇到偶数节点的时候我们不更新 pre，因此最后 pre 指向的一定是最后一个奇数节点
        pre.next = dummy_even_head.next
        return head