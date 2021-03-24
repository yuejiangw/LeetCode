class Solution:
    def compressString(self, S: str) -> str:
        if len(S) == 0:
            return S
        result = []
        counter = 1
        i = 0
        while i < len(S):
            j = i + 1
            while j < len(S) and S[j] == S[i]:
                j += 1
            result.append(S[i])
            result.append(j-i)
            i = j
        tmp = ''.join([str(x) for x in result])
        return S if len(tmp) >= len(S) else tmp
        