from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)
        for k, v in r.items():
            if k not in m.keys():
                return False
            else:
                if v > m[k]:
                    return False
        return True

# 2024.04.12
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return Counter(magazine) >= Counter(ransomNote)