from typing import List


class UnionFind:
    def __init__(self, n):
        self.count = n
        self.parent = [0] * n
        for i in range(n):
            self.parent[i] = i
    
    def _find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, p, q):
        r1, r2 = self._find(p), self._find(q)
        if r1 == r2:
            return
        self.parent[r1] = r2
        self.count -= 1
    

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    uf.union(i, j)
        return uf.count
