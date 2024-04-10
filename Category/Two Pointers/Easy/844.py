class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # O(1) 的空间复杂度，则不能使用 stack，采用双指针解法
        i, j = len(s) - 1, len(t) - 1   # 从后往前扫描字符串
        skipS, skipT = 0, 0             # 代表需要跳过几个字符
        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == '#':
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if t[j] == '#':
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:      # 某一个字符串先结束，说明处理后的字符串不一样长
                return False
            i -= 1
            j -= 1
        return True
