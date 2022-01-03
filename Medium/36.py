from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 记录某行，某位数字是否已经被摆放
        row = [[False] * 9 for _ in range(9)]
        # 记录某列，某位数字是否已经被摆放
        col = [[False] * 9 for _ in range(9)]
        # 3 * 3 * 9，三维数组，记录某宫格中某位数字是否已经被摆放
        block = [[[False for _ in range(9)]
                  for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    if row[i][num] or col[j][num] or block[i // 3][j // 3][num]:
                        return False
                    else:
                        row[i][num] = True
                        col[j][num] = True
                        block[i // 3][j // 3][num] = True
        return True
