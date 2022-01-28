from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # 按照攻击力降序，防御力升序排序
        properties = sorted(properties, key=lambda x: (-x[0], x[1]))
        res = 0
        max_defence = 0
        for _, defence in properties:
            if defence < max_defence:
                res += 1
            max_defence = max(max_defence, defence)
        return res
