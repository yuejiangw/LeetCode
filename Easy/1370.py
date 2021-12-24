from collections import Counter


class Solution:
    def sortString(self, s: str) -> str:
        """
        题目本质: 不断按字典序升序添加 → 降序添加，直到所有字符都出现在结果中
        """
        count = Counter(sorted(s))
        res = ''
        while len(res) < len(s):
            for k, v in count.items():
                if v > 0:
                    res += k
                    count[k] -= 1
            for k, v in reversed(count.items()):
                if v > 0:
                    res += k
                    count[k] -= 1
        return res
