from typing import List

class Solution:
    def append_space(self, line: List[str], total_len: int, maxWidth: int):
        """ 根据最大宽度向当前行的单词中间插入空格 """
        diff = maxWidth - total_len
        space_group_num = len(line) - 1
        # 如果当前行只有一个单词，则直接在该单词末尾补齐空格后返回即可
        if space_group_num == 0:
            return line[0] + ' ' * (maxWidth - total_len)
        # 如果当前行有 x 个单词，则这些单词两两中间有 x - 1 个位置需要我们插入空格
        # 已知所有单词的长度之和为 total_len，每行的最大长度为 maxWidth，因此我们
        # 需要将 (maxWidth - total_len) 个空格均匀地填充进 (x - 1) 个位置中。
        # 将这两数相除求商和余数，假设商和余数分别为 a 和 b，则我们可以构建一个长度为
        # (x - 1) 的数组，数组中前 b 个元素为长度为 (a + 1) 的空格字符串，剩余的元素
        # 为长度是 a 的空格字符串。将这些空格字符串插入到对应的位置即可。
        each_group_len = diff // space_group_num
        remain = diff % space_group_num
        space_arr = [' ' * each_group_len] * space_group_num
        for i in range(remain):
            space_arr[i] += ' '
        j = 0
        res = ''
        while j < len(space_arr):
            res += (line[j] + space_arr[j])
            j += 1
        res += line[j]
        return res

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i = 0
        res = []
        while i < len(words):
            curr_len = len(words[i])
            j = i + 1
            line = [words[i]]
            while j < len(words) and curr_len + len(line) + len(words[j]) <= maxWidth:
                line.append(words[j])
                curr_len += len(words[j])
                j += 1
            if j == len(words):
                tmp = ' '.join(line)
                tmp += (maxWidth - len(tmp)) * ' '
                res.append(tmp)
            else:
                tmp = self.append_space(line, curr_len, maxWidth)
                res.append(tmp)
            i = j
        return res
