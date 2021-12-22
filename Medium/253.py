from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 1

        length = len(intervals)
        start = [0] * length
        end = [0] * length
        for i in range(length):
            start[i] = intervals[i][0]
            end[i] = intervals[i][1]

        start.sort()
        end.sort()

        room = 0
        active_meeting = 0
        i, j = 0, 0
        while i < length and j < length:
            if start[i] < end[j]:
                active_meeting += 1
                i += 1
            else:
                active_meeting -= 1
                j += 1
            room = max(room, active_meeting)

        return room
