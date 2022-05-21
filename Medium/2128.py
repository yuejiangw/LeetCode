from typing import List


class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        # 只需要检查下面的每一行是否与第 0 行相等或者异或相等即可
        # T: O(mn)
        # S: O(1)
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return True

        def is_valid(row):
            """判断第 row 行与第 0 行是否相等或异或相等
            """
            diff_flag = grid[row][0] != grid[0][0]
            for j in range(n):
                if diff_flag:
                    if grid[row][j] == grid[0][j]:
                        return False
                else:
                    if grid[row][j] != grid[0][j]:
                        return False
            return True
        
        for i in range(1, m):
            if not is_valid(i):
                return False
        return True
        