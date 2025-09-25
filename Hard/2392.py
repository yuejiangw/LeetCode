class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        '''
        分别处理行和列，以优先级顺序建立有向图并进行拓扑排序
        T: O(k^2 + m + n)
        S: O(k + m + n)
        '''
        def topological_sort(conditions: List[List[int]], k: int):
            dependents = defaultdict(list)
            indegree = defaultdict(int)
            for x, y in conditions:
                dependents[x].append(y)
                indegree[y] += 1
            
            order = []
            queue = deque()
            # 数字范围是 1-k
            for i in range(1, k + 1):
                if indegree[i] == 0:
                    queue.append(i)
            while queue:
                curr = queue.popleft()
                order.append(curr)
                for dependent in dependents[curr]:
                    indegree[dependent] -= 1
                    if indegree[dependent] == 0:
                        queue.append(dependent)
            return order if len(order) == k else None

        if (row := topological_sort(rowConditions, k)) == None or (col := topological_sort(colConditions, k)) == None:
            return []
        # 先获得列坐标
        pos = {x: i for i, x in enumerate(col)}
        ans = [[0] * k for _ in range(k)]
        # 遍历行坐标
        for i, x in enumerate(row):
            ans[i][pos[x]] = x
        return ans
