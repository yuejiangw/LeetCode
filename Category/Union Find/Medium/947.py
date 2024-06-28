from collections import defaultdict
from typing import List


class UnionFind:
    def __init__(self, count):
        self.count = count  # count 是联通分量的个数
        self.parent = [0] * count
        for i in range(count):
            self.parent[i] = i
    
    def find(self, x):
        # 找到 x 的 parent node
        while self.parent[x] != x:
            # 压缩路径
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, p, q):
        # 合并两个联通分量
        p1, p2 = self.find(p), self.find(q)
        # 已经在同一组了
        if p1 == p2:
            return
        self.parent[p1] = p2
        self.count -= 1

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones) # 初始联通分量数为 n
        
        # 将二维坐标转换为一维坐标
        def encode(stone: List[int]):
            return stone[0] * 10000 + stone[1]
        
        row = defaultdict(list) # 记录横坐标相等的节点
        col = defaultdict(list) # 记录纵坐标相等的节点
        code_map = {}           # 记录一维坐标和 id 的映射关系
        for i, stone in enumerate(stones):
            code = encode(stone)
            code_map[code] = i
            row[stone[0]].append(code)
            col[stone[1]].append(code)

        # union find
        uf = UnionFind(n)

        for v in row.values():
            firstId = code_map[v[0]]
            for i in range(1, len(v)):
                uf.union(firstId, code_map[v[i]])
        for v in col.values():
            firstId = code_map[v[0]]
            for i in range(1, len(v)):
                uf.union(firstId, code_map[v[i]])
        
        return n - uf.count
