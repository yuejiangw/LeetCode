from typing import List


class Trie:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_word = False
    
    def insert(self, word):
        root = self
        for char in word:
            idx = ord(char) - ord('a')
            if not root.children[idx]:
                root.children[idx] = Trie()
            root = root.children[idx]
        root.is_word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        时间复杂度: 一共有 m * n 个搜索位置, 每次搜索四个方向, 最大深度不会超过 10, 因为每个 word 的最大长度不超过 10,
                  所以时间复杂度为 O(m * n * (4 ^ 10))
        空间复杂度: 对于 words 中全部的 word 都要进行搜索, 每搜索一次就要申请一次栈空间, 因此最大空间复杂度为 
                    O(sum(len(words[i]), i = 0, 1, ..., len(words) - 1)
        """
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        m, n = len(board), len(board[0])

        res = set()
        path = []
        visited = [[0] * n for _ in range(m)]

        def backtracking(trie, i, j):
            idx = ord(board[i][j]) - ord('a')
            if not trie.children[idx]:
                return
            
            path.append(board[i][j])
            visited[i][j] = 1

            child_trie = trie.children[idx]
            if child_trie.is_word:
                res.add(''.join(path))

            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and visited[x][y] == 0:
                    backtracking(child_trie, x, y)
            visited[i][j] = 0
            path.pop()

        for i in range(m):
            for j in range(n):
                backtracking(trie, i, j)
        return list(res)
