from typing import List
from collections import defaultdict


class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        # T: O(n^3)
        # S: O(n^2)
        n = len(scores)
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        # 枚举每一条边 (u, v)
        # 对于 u 和 v，分别枚举与其相邻的最大的三个点
        res = -1
        for i in range(n):
            graph[i].sort(key=lambda x: -scores[x])
        for u, v in edges:
            for x in graph[u][:3]:
                for y in graph[v][:3]:
                    if u != x and u != y and v != x and v != y and x != y:
                        res = max(res, scores[u] + scores[v] + scores[x] + scores[y])
        return res
