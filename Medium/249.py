from typing import List
from collections import defaultdict


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # 自定义哈希函数, 能通过移位得到的必须满足每位之间的差距相等
        # 时间复杂度: O(MN), M 是字符串的数量, N 是单个字符串的最大长度
        # 空间复杂度: O(M), 需要哈希表来辅助 
        def get_hash(s: str):
            return tuple((ord(s[i]) - ord(s[i - 1])) % 26 for i in range(1, len(s)))
        
        res = defaultdict(list)
        for s in strings:
            res[get_hash(s)].append(s)
        return list(res.values())