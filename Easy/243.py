from typing import List


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # T: O(N)
        # S: O(1)
        pos1, pos2 = -1, -1
        res = float('inf')
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                pos1 = i
            elif wordsDict[i] == word2:
                pos2 = i
            if pos1 != -1 and pos2 != -1:
                res = min(res, abs(pos1 - pos2))
        return res