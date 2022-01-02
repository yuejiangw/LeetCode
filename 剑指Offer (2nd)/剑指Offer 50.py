from collections import OrderedDict


class Solution:
    def firstUniqChar(self, s: str) -> str:
        count = OrderedDict()
        for c in s:
            if c not in count:
                count[c] = 1
            else:
                count[c] += 1
        for k, v in count.items():
            if v == 1:
                return k
        return ' '
