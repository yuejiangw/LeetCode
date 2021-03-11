class Solution:
    # 按照结束时间从小到大的顺序对interval进行排序
    def sortInterval(self, intervals: List[List[int]]) -> List[List[int]]:
        for i in range(len(intervals)-1):
            for j in range(i+1, len(intervals)):
                if intervals[i][1] > intervals[j][1]:
                    intervals[i], intervals[j] = intervals[j], intervals[i]
        return intervals
    
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # 如果只有一个interval，则直接返回0
        if len(intervals) == 0:
            return 0
        
        intervals = self.sortInterval(intervals)

        # 简单写法：利用sorted函数和lambda
        # intervals = sorted(intervals, key=lambda x : x[1])
        
        i = 1
        count = 0
        
        # 贪心思想，结束时间越早则后续空余的时间就越长
        while (i < len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                intervals.remove(intervals[i])
                count += 1
            else:
                i += 1
        return count