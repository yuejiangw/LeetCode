from typing import List


class UnionFind(object):
    def __init__(self):
        self.count = 26
        self.parent = [0] * 26
        for i in range(26):
            self.parent[i] = i
    
    def _find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, p, q):
        root_p, root_q = self._find(p), self._find(q)
        if root_p == root_q:
            return
        self.parent[root_p] = root_q
    
    def is_connected(self, p, q):
        return self._find(p) == self._find(q)


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # T: O(N)
        # S: O(1)
        uf = UnionFind()
        for equation in equations:
            if equation[1] == '=':
                a, b = equation[0], equation[3]
                uf.union(ord(a) - ord('a'), ord(b) - ord('a'))
        
        for equation in equations:
            if equation[1] == '!':
                a, b = equation[0], equation[3]
                if uf.is_connected(ord(a) - ord('a'), ord(b) - ord('a')):
                    return False
        return True
