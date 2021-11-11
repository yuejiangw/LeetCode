from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if matrix == [] or isinstance(matrix[0], list) == False:
            return matrix

        row = len(matrix)
        col = len(matrix[0])
        num = row * col

        up, print_up = 0, True
        right, print_right = col - 1, False
        bottom, print_bottom = row - 1, False
        left, print_left = 0, False

        res = []
        count = 0
        while count < num:
            if print_up:
                for j in range(left, right + 1):
                    res.append(matrix[up][j])
                    count += 1
                up += 1
                print_up, print_right = False, True

            elif print_right:
                for i in range(up, bottom + 1):
                    res.append(matrix[i][right])
                    count += 1
                right -= 1
                print_right, print_bottom = False, True

            elif print_bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                    count += 1
                bottom -= 1
                print_bottom, print_left = False, True

            elif print_left:
                for i in range(bottom, up - 1, -1):
                    res.append(matrix[i][left])
                    count += 1
                left += 1
                print_left, print_up = False, True

        return res
