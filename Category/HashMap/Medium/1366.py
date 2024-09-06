from typing import List
from collections import defaultdict


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        # T: O(NK + N^2logN), N 是数组 votes 中每个字符串的长度, k是数组 votes 的长度
        # S: O(N^2)
        score = defaultdict(lambda: [0] * len(votes[0]))
        for vote in votes:
            for i, char in enumerate(vote):
                score[char][i] -= 1
        res = sorted(votes[0], key=lambda x: (score[x], x))
        return ''.join(res)
        