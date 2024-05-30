from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5: 0, 10: 0, 20: 0}
        for i in range(len(bills)):
            if bills[i] == 5:
                change[5] += 1
            elif bills[i] == 10:
                if change[5] == 0:
                    return False
                else:
                    change[5] -= 1
                    change[10] += 1
            else:
                # 贪心策略：收到20元时，优先给1个10和1个5
                # 如果失败则尝试给3个5
                if change[10] > 0:
                    if change[5] > 0:
                        change[10] -= 1
                        change[5] -= 1
                        change[20] += 1
                    else:
                        return False
                else:
                    if change[5] >= 3:
                        change[5] -= 3
                        change[20] += 1
                    else:
                        return False

        return True
