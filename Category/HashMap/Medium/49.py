from typing import List
from collections import defaultdict

# 2024.04.12
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 关键在于对 s 进行编码
        # 设 strs 中最长的字符串长度为 n, strs 的长度为 m，则时间复杂度为 O(mn)
        # 空间复杂度为 O(m)
        def encode(s: str) -> str:
            chars = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                chars[idx] += 1
            return str(chars)
        
        group = defaultdict(list)
        for s in strs:
            key = encode(s)
            group[key].append(s)
        return list(group.values())


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        sorted_strs = {k: sorted(v) for k, v in enumerate(strs)}
        sorted_strs = sorted(sorted_strs.items(), key=lambda x: x[1])
        res = []
        group = [strs[sorted_strs[0][0]]]
        for i in range(1, len(sorted_strs)):
            if sorted_strs[i][1] == sorted_strs[i - 1][1]:
                group.append(strs[sorted_strs[i][0]])
            else:
                res.append(group[:])
                group = [strs[sorted_strs[i][0]]]
        res.append(group)
        return res


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        dic = {}
        for s in strs:
            k = ''.join(sorted(s))
            if k not in dic.keys():
                dic[k] = [s]
            else:
                dic[k].append(s)
        return list(dic.values())
