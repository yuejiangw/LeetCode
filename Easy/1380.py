from typing import List


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        res = []
        for row in matrix:
            min_num = min(row)
            col = row.index(min_num)
            is_lucky = True
            for i in range(len(matrix)):
                if matrix[i][col] > min_num:
                    is_lucky = False
                    break
            if is_lucky:
                res.append(min_num)
        return res