class Solution:
    def get_count(self, s: str):
        result = {}
        for char in s:
            if char in result.keys():
                result[char] += 1
            else:
                result[char] = 1
        return result

    def isPermutation(self, s1: str, s2: str) -> bool:
        return self.get_count(s1) == self.get_count(s2)

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        for i in range(0, len(s2) - len(s1) + 1):
            if self.isPermutation(s1, s2[i: i + len(s1)]):
                return True
        return False
        
from collections import defaultdict, Counter
class Solution:
    """ sliding window, O(n) """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = defaultdict(int)
        need = Counter(s1)
        i, j = 0, 0
        valid = 0
        while j < len(s2):
            c = s2[j]
            j += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            # shrink window
            while j - i >= len(s1):
                if valid == len(need):
                    return True
                d = s2[i]
                i += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return False
