from collections import defaultdict
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        cnt = defaultdict(int)
        for i in range(len(s) - 9):
            cnt[s[i: i + 10]] += 1
        return [k for k in cnt.keys() if cnt[k] > 1]

    