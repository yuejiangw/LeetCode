from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        i = 0
        while i < len(intervals) - 1:
            j = i + 1
            if intervals[j][0] >= intervals[i][0] and \
                    intervals[j][1] <= intervals[i][1]:
                del intervals[j]
            else:
                i += 1
        return len(intervals)


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        left = intervals[0][0]
        right = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            # overlap
            if left <= intervals[i][0] and right >= intervals[i][1]:
                res += 1
            # interaction
            elif right >= intervals[i][0] and right <= intervals[i][1]:
                right = intervals[i][1]
            # no connection
            elif right < intervals[i][0]:
                left = intervals[i][0]
                right = intervals[i][1]
        return len(intervals) - res
