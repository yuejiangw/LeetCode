from typing import List
from collections import defaultdict


# 2023-07-09
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        题目重点在于如何保证窗口内最多只有两种水果，即，我们应该动态调整
        哈希表，当其 value 为 0 时，就要将该元素从表中删除
        """
        l, r = 0, 0
        res = 0
        window = defaultdict(int)
        while r < len(fruits):
            c = fruits[r]
            r += 1
            window[c] += 1
            while len(window) > 2:
                d = fruits[l]
                l += 1
                window[d] -= 1
                if window[d] == 0:
                    del window[d]
            res = max(res, r - l)
        return res


# 2021-11-10
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """题意：选择只包含两个元素的最长子序列"""
        res = float("-inf")
        # chosen用来存放已经选取的水果
        chosen = {}
        idx = 0
        for i in range(len(fruits)):
            # 将当前水果装入篮子
            fruit = fruits[i]
            if fruit not in chosen.keys():
                chosen[fruit] = 1
            else:
                chosen[fruit] += 1

            # 如果种类超过两个，则将最先存入的元素的次数-1
            while len(chosen) > 2:
                first_fruit = fruits[idx]
                chosen[first_fruit] -= 1
                if chosen[first_fruit] == 0:
                    del chosen[first_fruit]
                idx += 1
            res = max(res, i - idx + 1)
        return res
