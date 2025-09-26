class UnionFind:
    def __init__(self, n):
        self.count = n
        self.parent = list(range(n))
    
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return self.parent[x]
    
    def union(self, x, y):
        r1, r2 = self.find(x), self.find(y)
        if r1 == r2:
            return
        self.parent[r1] = r2
        self.count -= 1

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 连通图 + 无环
        # 并查集判断：在无向图里，如果一条边的两个端点已经属于同一个连通分量，则一定有环
        if len(edges) != n - 1:
            return False
        uf = UnionFind(n)
        for a, b in edges:
            r1, r2 = uf.find(a), uf.find(b)
            if r1 == r2:
                return False
            uf.union(a, b)
        return True
