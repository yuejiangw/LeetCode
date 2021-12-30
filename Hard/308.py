from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

        row = len(self.matrix) + 1
        col = len(self.matrix[0]) + 1
        pre_sum = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(1, row):
            for j in range(1, col):
                pre_sum[i][j] = pre_sum[i][j-1] + pre_sum[i-1][j] \
                    - pre_sum[i-1][j-1] + self.matrix[i-1][j-1]

        self.pre_sum = pre_sum

    def update_pre(self, row, col):
        """
        传入的 row 和 col 是 matrix 的 row 和 col，
        对于 pre_sum 来说要把它们的坐标分别加1
        """
        row += 1
        col += 1
        for i in range(row, len(self.pre_sum)):
            for j in range(col, len(self.pre_sum[0])):
                self.pre_sum[i][j] = self.pre_sum[i][j-1] + self.pre_sum[i-1][j] \
                    - self.pre_sum[i-1][j-1] + self.matrix[i-1][j-1]

    def update(self, row: int, col: int, val: int) -> None:
        self.matrix[row][col] = val
        self.update_pre(row, col)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pre_sum[row2+1][col2+1] - self.pre_sum[row2+1][col1]\
            - self.pre_sum[row1][col2+1] + self.pre_sum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
