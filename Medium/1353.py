import heapq
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # T: O(nlogn)
        # S: O(n)
        events = sorted(events, key=lambda x: x[0])
        T = max([x[1] for x in events])
        heap = []
        j = 0
        n = len(events)
        res = 0
        # 枚举每一个可能的时刻
        for i in range(1, T + 1):
            # 删除过期的会议
            while heap and heap[0] < i:
                heapq.heappop(heap)
            # 加入可选会议
            while j < n and events[j][0] == i:
                heapq.heappush(heap, events[j][1])
                j += 1
            # 参加最早结束的会议
            if heap:
                heapq.heappop(heap)
                res += 1
        return res
