from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 如何确定是否能赶上前一辆车 - 出发位置远且到达时间久，则一定赶不上
        # 将车辆按照起始位置降序排序后，我们顺序扫描这些车辆。如果相邻的两辆车，前者比后者行驶到终点需要的时间短，那么后者永远追不上前者
        cars = sorted(zip(position, speed), reverse=True)
        res = 0
        curr_time = 0   # 当前 group 的到达时间
        for p, s in cars:
            arrival_time = (target - p) / s
            if arrival_time > curr_time:
                res += 1
                curr_time = arrival_time
        return res
