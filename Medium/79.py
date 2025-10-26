from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 不用全局变量的做法
        m, n = len(board), len(board[0])
        path = []
        visited = [[False] * n for _ in range(m)]

        def backtracking(i, j, start):
            if start == len(word):
                return True
            if i < 0 or j < 0 or i >= m or j >= n or word[start] != board[i][j] or visited[i][j]:
                return False
            visited[i][j] = True
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if backtracking(x, y, start + 1):
                    return True
            visited[i][j] = False
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtracking(i, j, 0):
                        return True
        return False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        length = len(word)
        is_find = False
        visited = [[0] * n for _ in range(m)]

        def backtracking(i, j, start_idx):
            """
            start_idx 记录目标单词的字符索引，只有棋盘格字符和 start_idx 指向的字符一致时，
            才会继续搜索接下来的字符；如果 start_idx 已经到达单词尾部了，则说明找到目标单词，
            将 is_find 标签修改为 True
            """
            nonlocal is_find
            if i < 0 or j < 0 or i >= m or j >= n or visited[i][j] == 1 \
                    or is_find or board[i][j] != word[start_idx]:
                return
            if start_idx == length - 1:
                is_find = True
                return

            visited[i][j] = True
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                backtracking(x, y, start_idx + 1)
            visited[i][j] = False

        for i in range(m):
            for j in range(n):
                backtracking(i, j, 0)
        return is_find


class Solution:
    """
    自己二次复习, 时间复杂度 O(MN . 4^k), 空间复杂度 O(k).
    M = 矩阵行数, N = 矩阵列数, k = 目标字符的长度
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def backtracking(i, j, start):
            if start == len(word):
                return True
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] == '#':
                return False
            if word[start] == board[i][j]:
                tmp = board[i][j]
                board[i][j] = '#'
                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if backtracking(x, y, start + 1):
                        return True
                board[i][j] = tmp
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtracking(i, j, 0):
                        return True
        return False
