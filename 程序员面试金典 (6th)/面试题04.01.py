from collections import defaultdict, deque
from typing import List


class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        # BFS
        # T: O(n)
        # S: O(n)
        adj = defaultdict(set)
        for g in graph:
            adj[g[0]].add(g[1])
        
        visited = set()
        queue = deque()
        queue.append(start)
        visited.add(start)
        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                if node == target:
                    return True
                for n in adj[node]:
                    if n not in visited:
                        visited.add(n)
                        queue.append(n)
        return False
