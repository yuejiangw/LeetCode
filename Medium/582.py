from collections import defaultdict, deque
from typing import List


class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        tree = defaultdict(list)
        for i in range(len(ppid)):
            parent, child = ppid[i], pid[i]
            tree[parent].append(child)
        # BFS
        res = []
        queue = deque()
        queue.append(kill)
        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                res.append(node)
                for child in tree[node]:
                    queue.append(child)
        return res
