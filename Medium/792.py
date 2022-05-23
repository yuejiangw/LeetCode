from typing import List
from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # len(s) = m, len(words) = n
        # T: O(m + sigma(len(word) for word in words))
        # S: O(n)
        bucket = defaultdict(list)
        res = 0
        for word in words:
            it = iter(word)
            bucket[next(it)].append(it)

        for char in s:
            old_bucket = bucket[char]
            bucket[char] = [] 
            while old_bucket:
                it = old_bucket.pop()
                nxt = next(it, None)
                if nxt:
                    bucket[nxt].append(it)
                else:
                    res += 1
        return res
