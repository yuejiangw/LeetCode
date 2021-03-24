class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        elif len(set(s1)) != len(set(s2)):
            return False
        else:
            for s in set(s1):
                if s not in set(s2):
                    return False
                if s1.count(s) != s2.count(s):
                    return False
            return True