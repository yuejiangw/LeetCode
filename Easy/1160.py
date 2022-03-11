from typing import List
from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def is_larger(c1, c2):
            for k, v in c2.items():
                if k not in c1:
                    return False
                elif k in c1 and c1[k] < v:
                    return False
            return True

        cnt_chars = Counter(chars)
        res = 0
        for word in words:
            cnt = Counter(word)
            if is_larger(cnt_chars, cnt):
                res += len(word)
        return res
