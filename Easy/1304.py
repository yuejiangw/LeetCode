from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        positive_half = list(range(1, n // 2 + 1))
        negative_half = [-x for x in positive_half]
        if n % 2 == 0:
            return positive_half + negative_half
        else:
            return positive_half + negative_half + [0]
