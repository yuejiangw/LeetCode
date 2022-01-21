from collections import defaultdict, deque
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        """ 转换成图用 bfs 做 """
        visited = set()
        visited.add(0)
        n = len(arr)
        target = arr[-1]
        graph = defaultdict(list[int])
        # 存储一个 num 在 arr 中的所有下标
        for i, num in enumerate(arr):
            graph[num].append(i)
        # 队列中存储 (index, step)
        queue = deque([(0, 0)])
        # BFS
        while queue:
            curr, step = queue.popleft()
            if curr == n - 1:
                return step
            for i in graph[arr[curr]]:
                if i not in visited:
                    queue.append((i, step + 1))
                    visited.add(i)
            # 访问过一个节点后，将其置空，防止多余的判断影响时间
            graph[arr[curr]] = []
            # 访问其相邻的前一个节点
            if curr > 0 and (curr - 1 not in visited):
                visited.add(curr - 1)
                queue.append((curr - 1, step + 1))
            # 访问其相邻的后一个节点
            if curr + 1 not in visited:
                visited.add(curr + 1)
                queue.append((curr + 1, step + 1))
        return n - 1
