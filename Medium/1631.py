import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        类似于 Dijkstra 的启发式搜索算法
        """
        # T: O(mnlog(mn))
        # S: O(mn)
        m, n = len(heights), len(heights[0])
        queue = [(0, 0, 0)]
        dp = [0] + [float('inf')] * (m * n - 1)
        visited = set()

        while queue:
            distance, i, j = heapq.heappop(queue)
            identifier = i * n + j
            if identifier in visited:
                continue
            if (i, j) == (m - 1, n - 1):
                break

            visited.add(identifier)
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < m and 0 <= y < n and \
                    max(distance, abs(heights[i][j] - heights[x][y])) <= dp[x * n + y]:
                    dp[x * n + y] = max(distance, abs(heights[i][j] - heights[x][y]))
                    heapq.heappush(queue, (dp[x * n + y], x, y))
        return dp[-1]

            