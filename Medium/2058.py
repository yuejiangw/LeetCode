# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # 第一个临界点下标
        min_point = None
        # 上一个临界点下标
        pre_point = None
        pre_val = None
        res = [float('inf'), float('-inf')]  # [min, max]
        idx = 0
        while head and head.next:
            if pre_val:
                curr = head.val
                next = head.next.val
                if (pre_val < curr and next < curr) or (pre_val > curr and next > curr):
                    if not min_point:
                        min_point = idx
                    if pre_point:
                        res[0] = min(res[0], idx - pre_point)
                        res[1] = max(res[1], idx - min_point)
                    pre_point = idx
            pre_val = head.val
            head = head.next
            idx += 1
        if res[0] == float('inf'):
            res[0] = -1
        if res[1] == float('-inf'):
            res[1] = -1
        return res
                