class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # 拓扑排序 + dp
        indegree = defaultdict(int)
        dependents = defaultdict(list)
        for pre, nxt in relations:
            indegree[nxt] += 1
            dependents[pre].append(nxt)
        
        res = 0
        queue = deque([i for i in range(1, n + 1) if indegree[i] == 0])
        # dp[i] 表示上完课程 i 需要的时间
        dp = [0] * (n + 1)
        while queue:
            curr = queue.popleft()
            dp[curr] += time[curr - 1]
            for d in dependents[curr]:
                # 状态转移，更新所有先修课程的耗时最大值
                dp[d] = max(dp[d], dp[curr])
                indegree[d] -= 1
                if indegree[d] == 0:
                    queue.append(d)
        return max(dp)