from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            path = [1] * (i + 1)
            for j in range(1, i):
                path[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(path)
        return res