from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        max_row = len(board)
        max_col = len(board[0])
        if not board or max_row == 0 or max_col == 0:
            return False

        visited = [[False for j in range(max_col)] for i in range(max_row)]

        def dfs(board, word, visited, i, j, k):
            if i < 0 or i >= max_row or j < 0 or j >= max_col \
                or board[i][j] != word[k] or visited[i][j]:
                return False
            if k == len(word) - 1:
                return True
            visited[i][j] = True
            res = dfs(board, word, visited, i - 1, j, k + 1) \
                    or dfs(board, word, visited, i, j - 1, k + 1) \
                    or dfs(board, word, visited, i + 1, j, k + 1) \
                    or dfs(board, word, visited, i, j + 1, k + 1)
            visited[i][j] = False   # 回溯，恢复标志位
            return res

        for i in range(max_row):
            for j in range(max_col):
                if dfs(board, word, visited, i, j, 0):
                    return True
        return False