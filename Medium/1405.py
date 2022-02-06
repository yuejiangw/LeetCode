class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        letters = [[a, 'a'], [b, 'b'], [c, 'c']]
        res = ''
        while True:
            for num in sorted(letters, key=lambda x: -x[0]):
                if num[0] <= 0:
                    return res
                if len(res) >= 2 and res[-2:] == num[1] * 2:
                    continue
                res += num[1]
                num[0] -= 1
                break
        return res
