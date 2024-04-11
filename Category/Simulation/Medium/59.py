from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = list(range(1, pow(n, 2) + 1))
        counts = pow(n, 2)
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        up = 0
        right = n - 1
        bottom = n - 1
        left = 0

        append_up = True
        append_right = False
        append_bottom = False
        append_left = False

        idx = 0
        while idx < counts:
            if append_up:
                for j in range(left, right + 1):
                    matrix[up][j] = nums[idx]
                    idx += 1
                up += 1
                append_up = False
                append_right = True

            elif append_right:
                for i in range(up, bottom + 1):
                    matrix[i][right] = nums[idx]
                    idx += 1
                right -= 1
                append_right = False
                append_bottom = True

            elif append_bottom:
                for j in range(right, left - 1, -1):
                    matrix[bottom][j] = nums[idx]
                    idx += 1
                bottom -= 1
                append_bottom = False
                append_left = True

            elif append_left:
                for i in range(bottom, up - 1, -1):
                    matrix[i][left] = nums[idx]
                    idx += 1
                left += 1
                append_left = False
                append_up = True

        return matrix
