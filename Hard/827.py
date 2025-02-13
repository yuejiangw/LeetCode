from collections import defaultdict
from collections import Counter
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # T: O(n^2), S: O(n^2)
        n = len(grid)
        island = defaultdict(int)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(i, j, visited, mark):
            if i < 0 or j < 0 or i >= n or j >= n or visited[i][j] == True or grid[i][j] == 0:
                return 0
            # 统计岛屿面积并且把所有陆地做上标记用来区分不同岛屿
            res = 1
            visited[i][j] = True
            grid[i][j] = mark
            for dx, dy in dirs:
                res += dfs(i + dx, j + dy, visited, mark)
            return res
        
        # 一次 dfs 求出各个岛屿的面积并记录
        all_island = True
        visited = [[False for _ in range(n)] for _ in range(n)]
        island_idx = 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    all_island = False
                if grid[i][j] == 1 and not visited[i][j]:
                    island[island_idx] = dfs(i, j, visited, island_idx)
                    island_idx += 1
        
        if all_island:
            return n * n

        # 遍历每个为 0 的方格 尝试将其变为 1 看看能否与周围岛屿连起来
        res = 0
        # 记录访问过的岛屿编号
        visited_island = set()
        for i in range(n):
            for j in range(n):
                # 记录连接之后的岛屿数量
                count = 1
                visited_island.clear()
                if grid[i][j] == 0:
                    for dx, dy in dirs:
                        neari, nearj = i + dx, j + dy
                        if neari < 0 or nearj < 0 or neari >= n or nearj >= n or grid[neari][nearj] in visited_island:
                            continue
                        count += island[grid[neari][nearj]]
                        visited_island.add(grid[neari][nearj])
                res = max(res, count)
        return res
