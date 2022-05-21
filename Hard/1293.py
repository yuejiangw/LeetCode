from collections import deque
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        # 从 (0,0) 走到 (m-1, n-1)，最多只可能有 m + n - 3 个障碍物
        # 如果已知 k >= m + n - 3，则可以直接返回理论最小值 m + n - 2
        if k >= m + n - 3:
            return m + n - 2
        
        queue = deque()
        visited = set()
        queue.append((0, 0, k))
        # 这里的去重需要注意，由于选择路径的变化，同一个方格可能有多种状态，所以这里的 visited
        # 要么使用三维数组来表示，要么使用 set 来存储三元组
        visited.add((0, 0, k))
        res = 0

        # BFS
        while queue:
            length = len(queue)
            for _ in range(length):
                i, j, r = queue.popleft()
                if i == m - 1 and j == n - 1 and r >= 0:
                    return res
                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= x < m and 0 <= y < n:
                        if grid[x][y] == 1 and r >= 1 \
                            and (x, y, r - 1) not in visited:
                            queue.append((x, y, r - 1))
                            visited.add((x, y, r - 1))
                        elif grid[x][y] == 0 and (x, y, r) not in visited:
                            queue.append((x, y, r))
                            visited.add((x, y, r))
            res += 1
        return -1
