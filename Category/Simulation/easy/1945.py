class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def str_2_num(s: str) -> int:
            res = ""
            for c in s:
                res += str(ord(c) - ord("a") + 1)
            return int(res)

        def transform_num(num: int) -> int:
            res = 0
            while num > 0:
                res += num % 10
                num = num // 10
            return res

        res = str_2_num(s)
        for i in range(k):
            if res // 10 == 0:
                break
            res = transform_num(res)
        return res
