from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        row = len(matrix)
        col = len(matrix[0])
        num = row * col

        up = 0
        right = col - 1
        bottom = row - 1
        left = 0

        print_up = True
        print_right = False
        print_bottom = False
        print_left = False

        count = 0
        while count < num:
            if print_up:
                for j in range(left, right + 1):
                    res.append(matrix[up][j])
                    count += 1
                up += 1
                print_up = False
                print_right = True

            elif print_right:
                for i in range(up, bottom + 1):
                    res.append(matrix[i][right])
                    count += 1
                right -= 1
                print_right = False
                print_bottom = True

            elif print_bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                    count += 1
                bottom -= 1
                print_bottom = False
                print_left = True

            elif print_left:
                for i in range(bottom, up - 1, -1):
                    res.append(matrix[i][left])
                    count += 1
                left += 1
                print_left = False
                print_up = True

        return res
