from collections import OrderedDict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_map = OrderedDict()
        for i, c in enumerate(s):
            if c in count_map:
                count_map[c][1] += 1
            else:
                count_map[c] = [i, 1]
        for v in count_map.values():
            if v[1] == 1:
                return v[0]
        return -1

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
        return -1
