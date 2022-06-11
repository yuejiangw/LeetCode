from collections import defaultdict, deque
from typing import List

class Solution:
    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:

        graph = defaultdict(set)
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        all_path = {}
        def get_path(start: int, curr: int, end: int, visited: set, path: List[int]):
            if curr == end:
                path.append(end)
                all_path[(start, end)] = set(path)
                return
            visited.add(curr)
            path.append(curr)
            for adj in graph[curr]:
                if adj not in visited:
                    get_path(start, adj, end, visited, path)
            path.pop()

        def bfs(target, path):
            queue =deque()
            seen = set()
            queue.append(target)
            seen.add(target)
            while queue:
                node = queue.popleft()
                if node in path:
                    return node
                for adj in graph[node]:
                    if adj not in seen:
                        seen.add(adj)
                        queue.append(adj)
            return -1

        res = []
        for i in range(len(query)):
            start, end, target = query[i]
            if (start, end) not in all_path:
                get_path(start, start, end, set(), [])
            res.append(bfs(target, all_path[(start, end)]))
        return res
