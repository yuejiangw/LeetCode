class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Greedy
        # 尽可能优先使用当前数量最多的字母，每次都要排序
        # T: O((a + b + c) * nlogn), 这里 n = 3（字母种类）
        # S: O(n) 这里 n = 3（字母种类）
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

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Greedy
        # 尽可能优先使用当前数量最多的字母，每次都要排序
        # T: O((a + b + c) * nlogn), 这里 n = 3（字母种类）
        # S: O(n) 这里 n = 3（字母种类）
        res = []
        letters = [[a, 'a'], [b, 'b'], [c, 'c']]
        while True:
            letters.sort(key=lambda x: -x[0])
            hasNext = False
            for i, (c, ch) in enumerate(letters):
                if c <= 0:
                    break
                if len(res) >= 2 and res[-2:] == [ch, ch]:
                    continue
                hasNext = True
                res.append(ch)
                letters[i][0] -= 1
                break
            if not hasNext:
                break
        return ''.join(res)