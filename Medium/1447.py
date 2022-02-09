from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(x, y):
            """ 辗转相除判断能否约分 """
            while y:
                t = x % y
                x = y
                y = t
            return x
        res = []
        for i in range(2, n + 1):
            for j in range(1, i):
                if gcd(i, j) == 1:
                    res.append(str(j) + '/' + str(i))
        return res
