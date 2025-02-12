# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import List
import heapq


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = curr = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = ListNode(l2.val)
                l2 = l2.next
            curr = curr.next
        
        curr.next = l1 if not l2 else l2
        return dummy.next
            
    def mergeSort(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = (left + right) // 2
        l1 = self.mergeSort(lists, left, mid)
        l2 = self.mergeSort(lists, mid + 1, right)
        return self.mergeTwoLists(l1, l2)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        多路归并排序，时间空间复杂度均为最优
        T: O(Nlogk)
        S: O(1)
        '''
        if not lists:
            return None
        return self.mergeSort(lists, 0, len(lists) - 1)


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