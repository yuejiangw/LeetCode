from typing import List


# 2025-09-22
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        '''
        建立反图
        T: O(m + n)
        S: O(m + n)
        '''
        n = len(graph)
        reverse_graph = defaultdict(list)
        indegree = defaultdict(int)
        for i, adj in enumerate(graph):
            indegree[i] += len(adj)
            for x in adj:
                reverse_graph[x].append(i)
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        res = [False for _ in range(n)]
        while queue:
            curr = queue.popleft()
            res[curr] = True
            for nxt in reverse_graph[curr]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        return [i for i, x in enumerate(res) if x == True]



class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res = []
        visited = set()

        def dfs(i):
            if i in visited:
                return False
            visited.add(i)
            for v in graph[i]:
                if not dfs(v):
                    return False
            visited.remove(i)
            graph[i] = []
            return True

        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        return res
