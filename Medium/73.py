from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # space complexity: O(m + n)
        row = set()
        col = set()

        row_len = len(matrix)
        col_len = len(matrix[0])

        for i in range(row_len):
            for j in range(col_len):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)

        for r in list(row):
            matrix[r] = [0] * col_len

        for c in list(col):
            for i in range(row_len):
                matrix[i][c] = 0

