from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Determine if there are intersections among these intervals.
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        for i in range(len(intervals) - 1):
            j = i + 1
            if intervals[j][0] < intervals[i][1]:
                return False
        return True
