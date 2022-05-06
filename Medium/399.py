from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # T: O(Q * (V + E))
        # S: O(V + E)
        graph = defaultdict(set)
        weight = defaultdict()
        # 建立图
        for i, equ in enumerate(equations):
            graph[equ[0]].add(equ[1])
            graph[equ[1]].add(equ[0])
            weight[tuple(equ)] = values[i]
            weight[(equ[1], equ[0])] = float(1 / values[i])

        def dfs(start, end, visited):
            # 图中已经有此边，直接输出
            if (start, end) in weight:
                return weight[(start, end)]
            # 节点不在图中，返回 -1
            if start not in graph or end not in graph:
                return -1.0
            # 节点已经访问过，返回0
            if start in visited:
                return 0

            visited.add(start)
            res = 0
            for node in graph[start]:
                res = dfs(node, end, visited) * weight[(start, node)]
                # 只要遍历到有一个不是0的解就输出
                if res != 0:
                    # 添加此边，节省访问时间
                    weight[(start, end)] = res
                    weight[(end, start)] = 1 / res
                    break
            visited.remove(start)
            return res

        res = []
        for start, end in queries:
            tmp = dfs(start, end, set())
            if tmp == 0:
                tmp = - 1.0
            res.append(tmp)
        return res
