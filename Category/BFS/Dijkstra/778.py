from typing import List
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """BFS
        只不过使用优先队列(堆)代替了普通的队列
        """
        # T: O(n^2 logn)
        # S: O(n^2)
        n = len(grid)
        res = 0
        heap = []
        visited = [[False] * n for _ in range(n)]
        heapq.heappush(heap, (grid[0][0], 0, 0))
        visited[0][0] = True

        while heap:
            length = len(heap)
            for _ in range(length):
                val, i, j = heapq.heappop(heap)
                res = max(res, val)
                if i == n - 1 and j == n - 1:
                    return res
                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= x < n and 0 <= y < n and not visited[x][y]:
                        heapq.heappush(heap, (grid[x][y], x, y))
                        visited[x][y] = True
        return res
            

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # dijkstra
        n = len(grid)
        heap = []
        visited = [[False for _ in range(n)] for _ in range(n)]
        distTo = [[float('inf') for _ in range(n)] for _ in range(n)]  # distTo[i][j] 代表 [0, 0] 到 [i, j] 所需的最小时间

        heapq.heappush(heap, (grid[0][0], 0, 0))
        distTo[0][0] = grid[0][0]

        while heap:
            val, i, j = heapq.heappop(heap)
            visited[i][j] = True
            if i == n - 1 and j == n - 1:
                return distTo[n - 1][n - 1]
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < n and 0 <= y < n and not visited[x][y]:
                    if max(distTo[i][j], grid[x][y]) < distTo[x][y]:
                        distTo[x][y] = max(distTo[i][j], grid[x][y])
                        heapq.heappush(heap, (grid[x][y], x, y))
        
        return distTo[n - 1][n - 1]