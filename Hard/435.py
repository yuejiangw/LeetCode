class Solution:
    def sortInterval(self, intervals: List[List[int]]) -> List[List[int]]:
        for i in range(len(intervals)-1):
            for j in range(i+1, len(intervals)):
                if intervals[i][1] > intervals[j][1]:
                    intervals[i], intervals[j] = intervals[j], intervals[i]
        return intervals
    
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        
        intervals = self.sortInterval(intervals)
        i = 1
        count = 0
        while (i < len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                intervals.remove(intervals[i])
                count += 1
            else:
                i += 1
        return count