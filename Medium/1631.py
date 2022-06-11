import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # T: O(mnlog(mn))
        # S: O(mn)
        m, n = len(heights), len(heights[0])
        queue = [(0, 0, 0)]
        # dp[i][j] 代表从 (0, 0) 走到 (i, j) 需要的小体力值
        dp = [[float('inf')] * n for _ in range(m)]
        dp[0][0] = 0

        while queue:
            distance, i, j = heapq.heappop(queue)
            if (i, j) == (m - 1, n - 1):
                break
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                # 首先满足点坐标合法
                if 0 <= x < m and 0 <= y < n:
                    # 之后判断当前这个点是不是一个较短路径
                    tmp = max(distance, abs(heights[i][j] - heights[x][y])) 
                    if tmp >= dp[x][y]:
                        continue
                    # 如果是的话需要相应地更新我们的 dp 数组, 并将该点入队列
                    dp[x][y] = tmp
                    heapq.heappush(queue, (tmp, x, y))
        return dp[-1][-1]