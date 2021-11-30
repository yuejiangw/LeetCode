from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        res = []

        def is_valid(board, i, j, n):
            # no queen on the same row or the same column
            for row in range(n):
                if board[row][j] == 'Q':
                    return False

            # no queen on left up, left down
            row = i - 1
            col = j - 1
            while row >= 0 and col >= 0:
                if board[row][col] == 'Q':
                    return False
                row -= 1
                col -= 1

            # no queen on right up, right down
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
