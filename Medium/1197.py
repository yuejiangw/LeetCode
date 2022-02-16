from collections import deque


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # bfs
        dirs = [(1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1), (-1, -2), (-2, -1)]
        res = 0
        queue = deque([(0, 0)])
        visited = {(0, 0)}
        while queue:
            length = len(queue)
            for _ in range(length):
                i, j = queue.popleft()
                if i == x and j == y:
                    return res
                for dx, dy in dirs:
                    new_x = i + dx
                    new_y = j + dy
                    if (new_x, new_y) not in visited:
                        queue.append((new_x, new_y))
                        visited.add((new_x, new_y))
            res += 1
        return res