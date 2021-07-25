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
        