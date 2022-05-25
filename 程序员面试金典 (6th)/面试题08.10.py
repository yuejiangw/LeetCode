from collections import deque
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # T: O(m * n)
        # S: O(m * n)
        m, n = len(image), len(image[0])
        visited = [[False] * n for _ in range(m)]
        queue = deque()
        queue.append((sr, sc))
        visited[sr][sc] = True
        oldColor = image[sr][sc]
        while queue:
            length = len(queue)
            for _ in range(length):
                i, j = queue.popleft()
                image[i][j] = newColor
                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= x < m and 0 <= y < n and not visited[x][y] \
                        and image[x][y] == oldColor:
                        queue.append((x, y))
                        visited[x][y] = True
        return image
