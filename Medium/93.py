from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def isValid(s):
            if not s:
                return False
            # 不能含有前导 0
            if len(s) > 1 and s[0] == '0':
                return False
            # 要在 0 - 255 之间
            return 0 <= int(s) <= 255

        res = []
        path = []
        def backtracking(start):
            if start == len(s):
                if len(path) == 4:
                    res.append('.'.join(path))
                return
            for i in range(start, len(s)):
                # 剪枝
                if len(path) > 4:
                    return
                substr = s[start: i + 1]
                if isValid(substr):
                    path.append(substr)
                    backtracking(i + 1)
                    path.pop()
        
        backtracking(0)
        return res