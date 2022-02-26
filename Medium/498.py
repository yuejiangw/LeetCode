from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or len(mat) == 0:
            return []
        r, c = 0, 0
        row, col = len(mat), len(mat[0])
        res = [0] * (row * col)
        for i in range(row * col):
            res[i] = mat[r][c]
            # r + c 为遍历的层数, 偶数向上遍历, 奇数向下遍历
            if (r + c) % 2 == 0:
                if c == col - 1:
                    # 往下移动一格准备向下遍历
                    r += 1
                elif r == 0:
                    # 往右移动一格准备向下遍历
                    c += 1
                else:
                    # 往上移动
                    r -= 1
                    c += 1
            else:
                if r == row - 1:
                    # 往右移动一格准备向上遍历
                    c += 1
                elif c == 0:
                    # 往下移动一格准备向上遍历
                    r += 1
                else:
                    r += 1
                    c -= 1
        return res