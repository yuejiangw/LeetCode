from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        elif len(points) == 1:
            return 1
        else:
            # 贪心算法，按照开始时间从小到大排序
            points = sorted(points, key=lambda x: x[0])
            arrow = 1
            i = 0
            min_end = points[i][1]
            j = 1
            while j < len(points):
                min_end = min(min_end, points[j][1])
                # 有重合部分，则arrow数量不变
                if points[j][0] <= min_end:
                    j += 1
                # 重合气球数量达到最大值，重新开始计数
                else:
                    i = j
                    min_end = points[i][1]
                    j = i + 1
                    arrow += 1
            return arrow


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[0])
        res = 0
        i = 0
        while i < len(points):
            min_end = points[i][1]
            j = i + 1
            while j < len(points):
                if points[j][0] <= min_end:
                    min_end = min(min_end, points[j][1])
                    j += 1
                else:
                    break
            res += 1
            i = j
        return res
