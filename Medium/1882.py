from heapq import heappop, heappush
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # m = len(servers), n = len(tasks)
        # T: O((m + n)logm)
        # S: O(m + n)

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
            # 下标为 i 的任务只能在时刻 i 开始，因此需要根据这个下标来更新 time
            time = max(time, i)
            # 更新了时间之后判断是否有已经执行完毕的任务
            release()
            # 如果没有空闲服务器的话直接将 time 更新为 busy_server 堆顶元素的时间，并将其释放
            if not free_server:
                time = busy_server[0][0]
                release()
            _, idx = heappop(free_server)
            res.append(idx)
            # 为当前任务分配服务器之后, 要将该服务器插入 busy_server 中
            heappush(busy_server, (time + task, idx))
        return res
