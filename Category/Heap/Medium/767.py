from collections import Counter
import heapq


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

class Solution:
    def reorganizeString(self, s: str) -> str:
        # T: O(n + nlogk)
        # S: O(k)
        # k 是不同字符的个数，n = len(s)
        cnt = Counter(s)
        heap = [(-v, k) for k, v in cnt.items()]
        heapq.heapify(heap)

        res = []
        while heap:
            count_first, char_first = heapq.heappop(heap)
            if not res or char_first != res[-1]:
                res.append(char_first)
                if count_first + 1 != 0:
                    heapq.heappush(heap, (count_first + 1, char_first))
            else:
                if not heap:
                    # 遇到重复字符且没有备选
                    return ''
                count_second, char_second = heapq.heappop(heap)
                res.append(char_second)
                if count_second + 1 != 0:
                    heapq.heappush(heap, (count_second + 1, char_second))
                heapq.heappush(heap, (count_first, char_first))
        return ''.join(res)