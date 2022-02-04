from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        path = []
        wordDict = set(wordDict)

        def backtracking(start):
            if start == len(s):
                res.append(" ".join(path))
                return
            for i in range(start, len(s)):
                word = s[start: i + 1]
                if word in wordDict:
                    path.append(word)
                    backtracking(i + 1)
                    path.pop()

        backtracking(0)
        return res
