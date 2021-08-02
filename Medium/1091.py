class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid is None or grid[0] is None \
           or len(grid) == 0 or len(grid[0]) == 0 \
           or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        # 8个方向
        direction = [
            [1, -1], [1, 0], [1, 1], [0, -1],
            [0, 1], [-1, -1], [-1, 0], [-1, 1]
        ]

        m = len(grid)
        n = len(grid[0])
        queue = [[0, 0]]
        grid[0][0] = 1
        path = 1
        while queue != []:
            size = len(queue)
            while size > 0:
                [x, y] = queue.pop(0)

                if x == m - 1 and y == n - 1:
                    return path
                
                for d in direction:
                    x1 = x + d[0]
                    y1 = y + d[1]

                    if x1 < 0 or x1 >= m or y1 < 0 or y1 >= m or grid[x1][y1] == 1:
                        continue
                    
                    queue.append([x1, y1])
                    grid[x1][y1] = 1
                size -= 1
            path += 1
        return -1