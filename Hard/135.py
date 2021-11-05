from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) < 2:
            return 1

        res = [1 for _ in range(len(ratings))]

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                res[i] = max(res[i], res[i + 1] + 1)

        return sum(res)
