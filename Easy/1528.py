class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = ['x'] * len(s)
        for i1, i2 in enumerate(indices):
            result[i2] = s[i1]
        return ''.join(result)