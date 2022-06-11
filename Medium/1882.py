from heapq import heappop, heappush
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # 空闲服务器，存储二元组 (w, idx)
        free_server = []
        # 忙碌服务器，存储二元组 (t, idx)
        busy_server = []
        for i, server in enumerate(servers):
            heappush(free_server, (server, i))

        time = 0
        res = []

        def release():
            # 将 busy_server 中满足 t <= time 的元素依次取出代表任务运行完成, 并放入 free_server 中
            while busy_server and busy_server[0][0] <= time:
                t, idx = heappop(busy_server)
                heappush(free_server, (servers[idx], idx))

        for i, task in enumerate(tasks):
            time = max(time, i)
            release()
            if not free_server:
                time = busy_server[0][0]
                release()
            _, idx = heappop(free_server)
            res.append(idx)
            heappush(busy_server, (time + task, idx))
        return res
