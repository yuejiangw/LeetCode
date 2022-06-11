class UnionFind(object):
    def __init__(self, n):
        self.count = n
        self.parent = [0] * n
        for i in range(n):
            self.parent[i] = i
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, p, q):
        r1, r2 = self.find(p), self.find(q)
        if r1 == r2:
            return
        self.parent[r1] = r2
        self.count -= 1

from typing import List

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # 排序 + 并查集
        # T: O(n + mlogm), m = len(logs)
        # S: O(n)
        logs = sorted(logs, key=lambda x: x[0])
        uf = UnionFind(n)
        curr_time = 0
        for log in logs:
            if uf.count == 1:
                break
            else:
                uf.union(log[1], log[2])
                curr_time = log[0]
        return curr_time if uf.count == 1 else -1
