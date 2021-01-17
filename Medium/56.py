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
