from typing import List

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        """思路
        贪心算法，维护一个 range 的左右边界值，遇到 I 的时候就将最小值插入，之后备选
        最小值 + 1，遇到 D 的时候就将最大值插入，之后备选最大值 - 1，最后将剩余的一个元素
        插入结果列表即可
        """
        # T: O(N)
        # S: O(1)
        min_num, max_num = 0, len(s)
        res = []
        for i in s:
            if i == 'I':
                res.append(min_num)
                min_num += 1
            else:
                res.append(max_num)
                max_num -= 1

        assert min_num == max_num
        res.append(min_num) # min_num == max_num
        return res
