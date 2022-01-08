from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        """ G(i) = i ^ (i / 2) """
        res = []
        for i in range(1 << n):
            res.append(i ^ (i >> 1))
        return res