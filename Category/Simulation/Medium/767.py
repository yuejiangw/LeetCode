from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        # 按照各个元素出现频率降序排列，会得到一个 list
        count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        # 如果某一个元素的出现频率大于 s 长度的一半，则一定会出现相邻字符
        if 2 * count[0][1] - 1 > len(s):
            return ''

        res = [''] * len(s)
        idx = 0
        for k, v in count:
            # 先按奇数下标插入再按偶数下标插入
            while v:
                res[idx] = k
                idx += 2
                v -= 1
                if idx >= len(s):
                    idx = 1
        return ''.join(res)