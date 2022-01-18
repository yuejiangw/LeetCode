from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # 从 0 到 24 小时一共只有 1440 分钟，若超过了这个 size 则说明一定有重复时间
        if len(timePoints) > 1440:
            return 0
        # 转换成分钟
        time = [int(t[:2]) * 60 + int(t[3:]) for t in timePoints]
        time.sort()

        res = 1440 + time[0] - time[-1]
        for i in range(len(time) - 1):
            if time[i + 1] - time[i] < res:
                res = time[i + 1] - time[i]
        return res
