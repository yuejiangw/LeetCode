import imp
from typing import List
from collections import defaultdict


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        """ 
        穿过砖块的数量最多为 len(wall), 若要找最少，则找数量最多的砖块对齐边缘,
        令 len(wall) - edges 则为最后结果
        """
        n = len(wall)
        edges = defaultdict(int)
        for i in range(n):
            prefix = 0
            for j in range(len(wall[i]) - 1):
                prefix += wall[i][j]
                edges[prefix] += 1
        return len(wall) - max(edges.values(), default=0)
