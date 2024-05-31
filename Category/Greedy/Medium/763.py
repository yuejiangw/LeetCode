from collections import OrderedDict
from collections import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 找最近结束位置划分
        # 记录字符出现的最后的位置
        position = {}
        for idx, val in enumerate(s):
            position[val] = idx
        
        res = []
        left = 0
        right = 0
        for i in range(len(s)):
            right = max(right, position[s[i]])
            if i == right:
                res.append(right - left + 1)
                left = i + 1
        return res


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        position = OrderedDict()
        for i in range(len(s)):
            if s[i] not in position:
                position[s[i]] = [i]
            else:
                position[s[i]].append(i)
        res = []
        i = 0
        max_idx = 0
        letters = list(position.keys())
        while i < len(s):
            char = s[i]
            max_idx = position[char][-1]
            candidate_idx = letters.index(char) + 1
            while candidate_idx < len(letters):
                candidate = letters[candidate_idx]
                if position[candidate][0] < max_idx:
                    max_idx = max(max_idx, position[candidate][-1])
                    candidate_idx += 1
                else:
                    break
            res.append(max_idx - i + 1)
            i = max_idx + 1
        return res
