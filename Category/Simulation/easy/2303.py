from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        # T: O(n)
        # S: O(1)
        res = 0
        for i in range(len(brackets)):
            upper, percent = brackets[i][0], brackets[i][1] * 0.01
            # 第一个元素，特殊处理
            if i == 0:
                if income >= upper:
                    res += upper * percent
                else:
                    res += income * percent
                    break
            # 后续元素
            else:
                pre_upper = brackets[i - 1][0]
                if income >= upper:
                    res += (upper - pre_upper) * percent
                else:
                    res += (income - pre_upper) * percent
                    break
        return res
