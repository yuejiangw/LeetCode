from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        res = []

        # is_valid 只检查了左上和右上还有同列，是因为我们是从上到下
        # 逐行放置棋子，当前行下面的行还没有放置
        def is_valid(board, i, j, n):
            # 检查列
            for row in range(n):
                if board[row][j] == 'Q':
                    return False

            # 检查左上
            row = i - 1
            col = j - 1
            while row >= 0 and col >= 0:
                if board[row][col] == 'Q':
                    return False
                row -= 1
                col -= 1

            # 检查右上
            row = i - 1
            col = j + 1
            while row < n and col < n:
                if board[row][col] == 'Q':
                    return False
                row -= 1
                col += 1

            return True

        def backtrack(board, row, n):
            # 结束条件：row 超过 board 的最后一行
            if row == n:
                tmp = []
                for row in board:
                    tmp.append(''.join(row))
                res.append(tmp)
                return

            for j in range(n):
                if not is_valid(board, row, j, n):
                    continue
                board[row][j] = 'Q'
                backtrack(board, row + 1, n)
                board[row][j] = '.'

        backtrack(board, 0, n)
        return res
