from math import log
from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = []
        # 为什么是 > 1 而不是 >= 1?
        # 因为如果是 >= 1 ，则在 = 1的时候计算对数会出错，因为label = label // 2 = 0
        # 所以只能是 > 1，最后在结果中把根节点[1]加上
        while label > 1:
            res.append(label)
            label = label // 2
            depth = int(log(label, 2))
            low = 2 ** depth
            high = low * 2 - 1
            # 由于之字形分布，因此根据上层的节点取值范围，修正父节点
            label = high - (label - low)
        return [1] + res[::-1]
