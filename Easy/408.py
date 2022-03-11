class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # T: O(N)
        # S: O(1)
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                # 不能有前导0
                if abbr[j] == '0':
                    return False
                start = j
                while j < len(abbr) and abbr[j].isdigit():
                    j += 1
                num = int(abbr[start: j])
                i += num
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        # 最后不能越界
        return i == len(word) and j == len(abbr)
