class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        先将所有出现在 order 中的字符取出来按顺序输入到结果中, 再将其他没有出现在 order 中的字符
        输出到结果中
        时间复杂度 O(N)
        空间复杂度 O(1)
        """
        cnt_s = [0] * 26
        for char in s:
            cnt_s[ord(char) - ord('a')] += 1
        res = ''
        for char in order:
            idx = ord(char) - ord('a')
            res += char * cnt_s[idx]
            cnt_s[idx] = 0

        for i in range(26):
            res += chr(i + 97) * cnt_s[i]
        return res