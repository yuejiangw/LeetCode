from typing import List


class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        n = len(s)
        mask = [False] * n
        for i in range(n):
            prefix = s[i:]
            for word in words:
                if prefix.startswith(word):
                    for j in range(i, min(i + len(word), n)):
                        mask[j] = True
        
        res = []
        for i in range(n):
            if mask[i] and (i == 0 or not mask[i - 1]):
                res.append('<b>')
            res.append(s[i])
            if mask[i] and (i == n - 1 or not mask[i + 1]):
                res.append('</b>')
        return ''.join(res)
