from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        X = [0, 0, -1, 1, -1, -1, 1, 1]
        Y = [-1, 1, 0, 0, -1, 1, -1, 1]
        row = len(board)
        col = len(board[0])

        def is_valid(i, j):
            return 0 <= i < row and 0 <= j < col

        def find_mine(i, j):
            res = 0
            for k in range(8):
                x, y = i + X[k], j + Y[k]
                if is_valid(x, y) and board[x][y] == 'M':
                    res += 1
            return res

        def dfs(i, j):
            if not is_valid(i, j):
                return
            if board[i][j] == 'E':
                mine_num = find_mine(i, j)
                if mine_num == 0:
                    board[i][j] = 'B'
                    for k in range(8):
                        dfs(i + X[k], j + Y[k])
                else:
                    board[i][j] = str(mine_num)

        x, y = click
        if board[x][y] == 'E':
            dfs(x, y)
        elif board[x][y] == 'M':
            board[x][y] = 'X'
        return board
