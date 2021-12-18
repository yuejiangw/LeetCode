class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:

        visited = [[False for _ in range(n)] for _ in range(m)]
        def dfs(m, n, i, j, k, visited):
            digit_sum = i // 10 + i % 10 + j // 10 + j % 10
            if i < 0 or i > m - 1 or j < 0 or j > n - 1 or digit_sum > k or visited[i][j]:
                return 0
            visited[i][j] = True
            return dfs(m, n, i + 1, j, k, visited) + dfs(m, n, i - 1, j, k, visited) + \
                   dfs(m, n, i, j + 1, k, visited) + dfs(m, n, i, j - 1, k, visited) + 1
        
        return dfs(m, n, 0, 0, k, visited)