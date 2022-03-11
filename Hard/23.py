# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import List
import heapq


class Solution:
    def to_list(self, head):
        curr = head
        res = []
        while curr:
          res.append(curr.val)
          curr = curr.next
        return res

    def list_to_link(self, l):
        head = ListNode()
        curr = head
        for num in l:
            curr.next = ListNode(num)
            curr = curr.next
        return head.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        nums = []
        for i in range(len(lists)):
            nums += self.to_list(lists[i])
        nums.sort()
        return self.list_to_link(nums)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # T: O(NlogK), N 是所有链表中节点的数量总和, k 是链表个数
        # S: O(K)
        dummy = ListNode()
        cur = dummy
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        while heap:
            val, idx = heapq.heappop(heap)
            cur.next = ListNode(val)
            cur = cur.next
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next