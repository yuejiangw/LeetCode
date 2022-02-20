from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        先将矩阵按照左上到又下的对角线进行对称, 然后从左到右 reverse 每一行即可
        时间复杂度: O(N^2), N 是矩阵边长
        空间复杂度: O(1), 因为是原地翻转
        """
        n = len(matrix)
        if n == 1:
            return
        # 一个坑: j 需要从 i 开始遍历, 否则会覆盖之前的翻转结果
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()
        