from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def encode(s: str) -> str:
            count = [0] * 26
            for c in s:
                delta = ord(c) - ord("a")
                count[delta] += 1
            return str(count)

        groups = {}
        for s in strs:
            code = encode(s)
            if code not in groups:
                groups[code] = []
            groups[code].append(s)
        return list(groups.values())
