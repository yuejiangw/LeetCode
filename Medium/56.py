class Solution:

    def selectionSort(self, intervals: List[List[int]]):
        for i in range(len(intervals) - 1):
            k = i
            for j in range(k + 1, len(intervals)):
                if intervals[j][0] < intervals[k][0]:
                    k = j
            if k != i:
                tmp = intervals[i]
                intervals[i] = intervals[k]
                intervals[k] = tmp

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        self.selectionSort(intervals)
        result = []
        for i in range(len(intervals) - 1):
            if intervals[i][1] >= intervals[i + 1][0]:
                intervals[i + 1][0] = intervals[i][0]
                intervals[i + 1][1] = intervals[i][1] if intervals[i + 1][1] < intervals[i][1] else intervals[i + 1][1]
            else:
                result.append(intervals[i])
        # 处理最后一个区间
        result.append(intervals[-1])
        return result

from typing import List
import heapq

class Solution:
    """ Time and Space Complexity: O(N) """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        i = 0
        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]
            j = i + 1
            while j < len(intervals) and intervals[j][0] <= end:
                end = max(end, intervals[j][1])
                j += 1
            res.append([start, end])
            i = j
        return res
