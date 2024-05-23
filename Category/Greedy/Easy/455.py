# 从饥饿度最小的孩子开始，分配最小的饼干
# 若可以分配，则满足的孩子数量+1
# 无论是否可以满足孩子，饼干数量都要不断+1，因为一个孩子只能至多吃一块饼干

from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child, cookie = 0, 0
        while (child < len(g) and cookie < len(s)):
            if g[child] <= s[cookie]:
                child += 1
            cookie += 1
        return child

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()    # child
        s.sort()    # cookie
        idx = 0
        for i in range(len(s)):
            if idx < len(g) and s[i] >= g[idx]:
                idx += 1
        return idx
