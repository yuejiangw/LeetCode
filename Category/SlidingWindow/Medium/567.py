from collections import Counter, defaultdict


# 2023-07-12
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        题目翻译：在 s2 中是否存在这样一个子串，它是 s1 的异位词
        设 m = len(s1), n = len(s2)
        T: O(m + n * 26)
        S: O(26 * 2)
        """
        l, r = 0, 0
        cnt = Counter(s1)
        window = defaultdict(int)
        while r < len(s2):
            c = s2[r]
            r += 1
            window[c] += 1

            while window.keys() >= cnt.keys() and all(
                window[k] >= v for k, v in cnt.items()
            ):
                if window == cnt:
                    return True
                print(window)
                d = s2[l]
                l += 1
                window[d] -= 1
                if window[d] == 0:
                    del window[d]

        return False


# 2023-07-14
class Solution:
    """sliding window, O(n)"""

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


# 2023-07-14
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
            if self.isPermutation(s1, s2[i : i + len(s1)]):
                return True
        return False
