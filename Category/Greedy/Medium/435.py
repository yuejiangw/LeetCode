from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 按照区间终点排序
        intervals.sort(key=lambda x: x[1])
        # 记录非重叠区间的个数
        count = 1
        min_right = intervals[0][1]
        for i in range(1, len(intervals)):
            # 不重叠
            if min_right <= intervals[i][0]:
                min_right = intervals[i][1]
                count += 1
        return len(intervals) - count