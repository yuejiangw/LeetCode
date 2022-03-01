from typing import List


class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        # T: O(N * sum(w_i)), w_i 是 words 中各个单词的长度
        # S: O(N)
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