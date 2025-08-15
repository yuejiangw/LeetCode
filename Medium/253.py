from typing import List
from heapq import heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # T: O(nlogn), S: O(n)
        # 按照开始时间排序
        intervals.sort(key=lambda x: x[0])
        
        # 小顶堆，存结束时间
        heap = []
        for start, end in intervals:
            if heap and heap[0] <= start:
                heappop(heap)
            heappush(heap, end)
        return len(heap)



class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        num = 0
        res = float('-inf')
        start = sorted([interval[0] for interval in intervals])
        end = sorted([interval[1] for interval in intervals])

        i, j = 0, 0
        while i < len(intervals) and j < len(intervals):
            if start[i] < end[j]:
                num += 1
                i += 1
            else:
                num -= 1
                j += 1
            res = max(num, res)
        return res
