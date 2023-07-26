from typing import List


class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        """
        [3, 2, 0, 2] => [2, 0, 2, 3]
        2
        0 + 1/2 = 1/2
        2 + 1/(1/2) = 4
        3 + 1/4 = 13/4
        """
        res = [1, 0]
        for num in cont[::-1]:
            tmp = res[1]
            res[1] = res[0]
            res[0] = num * res[1] + tmp
        return res
