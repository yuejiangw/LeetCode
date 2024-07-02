from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
             idx
          i
          j

        """
        # i 和 j 分别代表当前处理到的位置和答案待插入位置
        n = len(chars)
        if n == 1:
            return n
        i, j = 0, 0
        while i < n:
            # 找相同字符
            idx = i
            while idx < n and chars[idx] == chars[i]:
                idx += 1
            cnt = idx - i
            # 更新
            chars[j] = chars[i]
            j += 1
            if cnt > 1:
                for c in str(cnt):
                    chars[j] = c
                    j += 1
            # 移动 i
            i = idx        
        return j