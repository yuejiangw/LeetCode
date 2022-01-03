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


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # use the first row and the first column as the mark
        # so we only need two other flag
        # space complexity: O(1)
        row = len(matrix)
        col = len(matrix[0])

        flag_row = any(matrix[0][j] == 0 for j in range(col))
        flag_col = any(matrix[i][0] == 0 for i in range(row))

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if flag_row:
            for j in range(col):
                matrix[0][j] = 0

        if flag_col:
            for i in range(row):
                matrix[i][0] = 0
