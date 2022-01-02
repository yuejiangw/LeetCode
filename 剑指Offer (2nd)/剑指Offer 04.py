from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == [] or len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        row = len(matrix)
        col = len(matrix[0])

        i = row - 1
        j = 0
        while i >= 0 and j < col:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
        return False
