from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        res = []
        left, right = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= right:
                right = max(right, intervals[i][1])
            else:
                res.append([left, right])
                left, right = intervals[i]
        res.append([left, right])
        return res


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        res = []
        for interval in intervals:
            if not res or interval[0] > res[-1][1]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x: (x[0], x[1]))
        i = 0
        while i < len(intervals):
            start, end = intervals[i]
            j = i + 1
            while j < len(intervals) and intervals[j][0] <= end:
                start = min(start, intervals[j][0])
                end = max(end, intervals[j][1])
                j += 1
            i = j
            res.append([start, end])
        return res
