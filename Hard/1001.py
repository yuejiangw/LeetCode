from collections import defaultdict
from typing import List


class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        open_lamps = set()    # 目前开启的灯泡
        row, col = defaultdict(int), defaultdict(int)   # 行，列
        diag, antidiag = defaultdict(int), defaultdict(int) # 对角线，反对角线
        
        for i, j in lamps:
            if (i, j) not in open_lamps:
                open_lamps.add((i, j))
                row[i] += 1
                col[j] += 1
                # 对角线，j - i 为常数
                diag[j - i] += 1
                # 反对角线，i + j 为常数
                antidiag[i + j] += 1
        
        ans = []
        for i, j in queries:
            # 先判断是否被照亮，只要是在被照亮的某个字典中即可
            if row[i] or col[j] or diag[j - i] or antidiag[i + j]:
                ans.append(1)
            else:
                ans.append(0)
                continue
            
            # 关闭附近的灯泡
            for x, y in [(i, j), (i - 1, j), (i - 1, j - 1), (i - 1, j + 1),\
                    (i + 1, j), (i + 1, j - 1), (i + 1, j + 1), (i, j + 1), (i, j - 1)]:
                if (x, y) in open_lamps:
                    open_lamps.remove((x, y))
                    row[x] -= 1
                    col[y] -= 1
                    diag[y - x] -= 1
                    antidiag[x + y] -= 1
        return ans