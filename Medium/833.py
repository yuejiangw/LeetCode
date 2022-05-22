from collections import defaultdict
from typing import List


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # T: O(M + N), M = len(s)
        # S: O(N)

        replace = defaultdict(list)
        for i in range(len(indices)):
            replace[indices[i]] = [sources[i], targets[i]]
        i = 0
        res = ''
        while i < len(s):
            if i in replace:
                source, target = replace[i][0], replace[i][1]
                if s[i: i + len(source)] == source:
                    res += target
                else:
                    res += s[i: i + len(source)]
                i += len(source)
            else:
                res += s[i]
                i += 1
        return res
