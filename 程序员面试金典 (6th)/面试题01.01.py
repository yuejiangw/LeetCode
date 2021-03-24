class Solution:
    def isUnique(self, astr: str) -> bool:
        for s in astr:
            if astr.count(s) != 1:
                return False
        return True