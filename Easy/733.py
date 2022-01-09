from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        old_color = image[sr][sc]

        def dfs(x, y):
            if x < 0 or x >= row or y < 0 or y >= col:
                return
            if image[x][y] != old_color or image[x][y] == newColor:
                return
            image[x][y] = newColor
            dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
            for i in range(4):
                dfs(x + dx[i], y + dy[i])
        
        dfs(sr, sc)
        return image