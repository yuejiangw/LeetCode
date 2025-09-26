class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # 拓扑排序 + BFS
        if len(prerequisites) == 0:
            return [False] * len(queries)
        
        indegree = defaultdict(int)
        dependents = defaultdict(list)
        for a, b in prerequisites:
            indegree[b] += 1
            dependents[a].append(b)
        
        isPre = [[False] * numCourses for _ in range(numCourses)]
        queue = deque([x for x in list(range(numCourses)) if indegree[x] == 0])

        while queue:
            curr = queue.popleft()
            for dependent in dependents[curr]:
                isPre[curr][dependent] = True
                for i in range(numCourses):
                    # 如果 i 是 curr 的先修，则根据传递关系 i 也应该是 dependent 的先修
                    isPre[i][dependent] = isPre[i][curr] or isPre[i][dependent]
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    queue.append(dependent)
        
        res = []
        for u, v in queries:
            res.append(isPre[u][v])
        return res
        