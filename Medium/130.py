from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= row or j >= col:
                return
            if board[i][j] == 'X' or board[i][j] == 'A':
                return
            board[i][j] = 'A'
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(i + dx, j + dy)

        for i in range(row):
            dfs(i, 0)
            dfs(i, col - 1)
        for j in range(col):
            dfs(0, j)
            dfs(row - 1, j)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'A':
                    board[i][j] = 'O'

from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])

        def bfs(i, j):
            queue = deque()
            visited = [[0] * col for _ in range(row)]
            queue.append((i, j))
            visited[i][j] = 1
            while queue:
                length = len(queue)
                for _ in range(length):
                    x, y = queue.popleft()
                    if board[x][y] == 'X' or board[x][y] == 'A':
                        continue
                    board[x][y] = 'A'
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        x_next = x + dx
                        y_next = y + dy
                        if 0 <= x_next < row and 0 <= y_next < col \
                                and not visited[x_next][y_next]:
                            queue.append((x_next, y_next))
                            visited[x_next][y_next] = 1

        # 将矩形四条边上所有的'O'都变成'A'
        for i in range(row):
            bfs(i, 0)
            bfs(i, col - 1)
        for j in range(col):
            bfs(0, j)
            bfs(row - 1, j)

        # 由于矩形边上所有的'O'都已经变成了'A'，因此遍历矩阵时剩下的'O'就是被围绕的'O'
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'A':
                    board[i][j] = 'O'
