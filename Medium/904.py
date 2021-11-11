from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """题意：选择只包含两个元素的最长子序列"""
        res = float('-inf')
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
