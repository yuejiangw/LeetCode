class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        res = '1'
        for _ in range(1, n):
            tmp = ''
            i, j = 0, 1
            while i < len(res):
                while j < len(res) and res[i] == res[j]:
                    j += 1
                tmp += str(j - i) + res[i]
                i = j
            res = tmp
        return res
