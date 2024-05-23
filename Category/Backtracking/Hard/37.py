from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(i, j, k, board):
            # 每一行只出现一次
            for col in range(9):
                if board[i][col] == k:
                    return False
            # 每一列只出现一次
            for row in range(9):
                if board[row][j] == k:
                    return False
            # 3 * 3 宫内只出现一次
            # 通过 i, j 求出该宫的最左上角的坐标
            row, col = (i // 3) * 3, (j // 3) * 3
            for m in range(row, row + 3):
                for n in range(col, col + 3):
                    if board[m][n] == k:
                        return False
            return True

        def backtracking(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    # 如果不是需要填数字的空位则跳过
                    if board[i][j] != '.':
                        continue
                    # 从 1 到 10 逐个判断该数字是否合适
                    for k in range(1, 10):
                        str_k = str(k)
                        if is_valid(i, j, str_k, board):
                            board[i][j] = str_k
                            if backtracking(board):
                                return True
                            board[i][j] = '.'
                    # 9 个数都试了一遍还是不行则直接 return False
                    return False
            # 没有 return False 说明找到了合适的棋盘位置
            return True
        
        backtracking(board)
