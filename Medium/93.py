from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        path = []
        def backtracking(s, start_index):
            if start_index == len(s):
                if len(path) == 4:
                    res.append('.'.join(path))
                return

            for i in range(start_index, len(s)):
                # 剪枝策略：当path中的字符串超过4个的时候肯定不满足
                # IP地址格式，则直接结束当前循环
                if len(path) >= 4:
                    break
                p = s[start_index: i + 1]
                num = int(p)    # 优化小技巧：将int(p)单独设一个临时变量num
                if num >= 0 and num <= 255:
                    if len(p) > 1 and p[0] == '0':
                        break
                    else:
                        path.append(p)
                        backtracking(s, i + 1)
                        path.pop()
                else:
                    break
        backtracking(s, 0)
        return res