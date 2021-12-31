from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []

        res = [[0 for _ in range(n)] for _ in range(m)]
        i = 0
        for j in range(0, len(original), n):
            res[i] = original[j: j+n]
            i += 1
        return res
